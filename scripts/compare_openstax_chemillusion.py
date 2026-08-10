#!/usr/bin/env python3
"""Full-book quantitative comparison of OpenStax Organic Chemistry and ChemIllusion.

Analyses implemented
--------------------
4. Textual overlap / independence
   * exact token n-grams for configurable phrase lengths
   * longest exact contiguous token run
   * exact matching blocks at or above a configurable minimum length

7. Identical molecule counts
   * ChemIllusion molecule blocks are canonicalized with RDKit
   * a molecule is counted as shared when an auditable alias for that exact
     canonical ChemIllusion structure appears in the OpenStax chapter text
   * no fingerprint or Tanimoto similarity is calculated

8. Figure / visual comparison
   * unique numbered OpenStax figures and tables from PDF-extracted captions
   * visible ChemIllusion visual blocks from compiled reader JSON
   * taxonomy counts only; no visual-density output

The script can read compiled chapters from a local source tree or from a
previously generated snapshot JSON used for testing.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import unicodedata
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable, Sequence

import fitz  # PyMuPDF
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
from rdkit import Chem

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - optional until requirements are installed
    load_dotenv = None

DEFAULT_OPENSTAX_URL = (
    "https://assets.openstax.org/oscms-prodcms/media/documents/"
    "organic-chemistry_-_WEB.pdf"
)
DEFAULT_OPENSTAX_CACHE_FILENAME = "openstax-organic-chemistry-current.pdf"

DEFAULT_CHAPTERS = tuple(range(1, 32))
DEFAULT_NGRAM_SIZES = (5, 8, 12, 16, 20)
DEFAULT_MIN_MATCH_BLOCK = 8

INK = "#1F2937"
MUTED_INK = "#52606D"
GRID = "#D7DEE7"
BLUE = "#2563EB"
BLUE_DARK = "#1E3A8A"
BLUE_LIGHT = "#DBEAFE"
GOLD = "#C58B00"
PLOT_BACKGROUND = "#FFFFFF"
HEATMAP_CMAP = LinearSegmentedColormap.from_list(
    "chemillusion_blue",
    ["#F8FAFC", BLUE_LIGHT, BLUE, BLUE_DARK],
)

TEXT_BLOCK_TYPES = {"text"}
NON_VISUAL_BLOCK_TYPES = {
    "text",
    "external_link",
    "mcmurry_link",
    "tutorial",
    "chat_tool",
    "homework_preview",
}

GENERIC_MOLECULE_ASSET_TERMS = {
    "table",
    "chart",
    "relationship",
    "range",
    "representative",
    "four factors",
    "electron-pair donation",
    "association",
    "displacement",
    "equilibrium direction",
    "comparison",
    "summary",
    "overview",
    "trend",
}


@dataclass(frozen=True)
class ChapterSpec:
    chapter: int
    slug: str
    title: str


@dataclass(frozen=True)
class ChapterCorpus:
    chapter: int
    openstax_raw: str
    openstax_clean: str
    chemillusion_text: str


@dataclass
class MoleculeRecord:
    canonical_smiles: str
    preferred_name: str
    aliases: set[str]
    source_names: set[str]


def warn(message: str) -> None:
    print(f"WARNING: {message}", file=sys.stderr)


def file_fingerprint(path: Path) -> dict[str, Any]:
    """Return a stable, auditable fingerprint for one input file."""
    resolved = path.expanduser().resolve()
    digest = hashlib.sha256()
    with resolved.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    stat = resolved.stat()
    return {
        "path": str(resolved),
        "size_bytes": stat.st_size,
        "sha256": digest.hexdigest(),
        "modified_at_utc": datetime.fromtimestamp(
            stat.st_mtime, tz=timezone.utc
        ).isoformat(),
    }


def _display_fingerprint(path: Path, display_path: str) -> dict[str, Any]:
    fingerprint = file_fingerprint(path)
    fingerprint["path"] = display_path
    return fingerprint


def git_source_metadata(
    root: Path | None, selected_relative_paths: set[str]
) -> dict[str, Any]:
    """Return public-safe provenance for the selected authored inputs only."""
    if root is None:
        return {"source_commit": None, "selected_inputs_dirty": False}

    def run(*arguments: str) -> str | None:
        completed = subprocess.run(
            ["git", "-C", str(root), *arguments],
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
        )
        return completed.stdout.rstrip("\r\n") if completed.returncode == 0 else None

    status_text = run("status", "--short") or ""
    status = [line for line in status_text.splitlines() if line]
    dirty_paths = [
        line[3:].split(" -> ")[-1]
        for line in status
        if len(line) > 3
    ]
    return {
        "source_commit": run("rev-parse", "HEAD"),
        "selected_inputs_dirty": any(
            path in selected_relative_paths for path in dirty_paths
        ),
    }


def chapter_source_manifest_record(
    *, chapter: int, spec: ChapterSpec, compiled_chapter: dict[str, Any]
) -> dict[str, Any]:
    """Describe one compiled chapter without exposing its local input path."""
    compiled_source = Path(str(compiled_chapter.get("source_path", "")))
    compiled_sha256 = (
        file_fingerprint(compiled_source)["sha256"]
        if compiled_source.is_file()
        else ""
    )
    return {
        "chapter": chapter,
        "slug": spec.slug,
        "compiled_source_sha256": compiled_sha256,
        "compiled_source_available": bool(compiled_chapter.get("available", False)),
    }


def build_run_manifest(
    *,
    openstax_pdf: Path,
    openstax_url: str,
    openstax_page_count: int,
    chemillusion_root: Path | None,
    chemillusion_provenance_root: Path | None,
    selected_specs: Sequence[ChapterSpec],
    selected_chapters: Sequence[int],
    ngram_sizes: Sequence[int],
    min_match_block: int,
    script_path: Path,
    chapter_map_path: Path,
    molecule_aliases_path: Path,
    command: Sequence[str],
    openstax_metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build the complete reproducibility record for a comparison run."""
    source_root = chemillusion_provenance_root
    package_root = chemillusion_root or source_root
    packages: list[dict[str, Any]] = []
    selected_relative_paths: set[str] = set()
    for spec in selected_specs:
        relative = Path(
            f"content/organic/topic-packages/{spec.slug}/topic.package.json"
        )
        selected_relative_paths.add(relative.as_posix())
        package_path = package_root / relative if package_root else relative
        record: dict[str, Any] = {
            "chapter": spec.chapter,
            "slug": spec.slug,
            "exists": package_path.is_file(),
        }
        if package_path.is_file():
            fingerprint = file_fingerprint(package_path)
            record.update(
                {
                    "size_bytes": fingerprint["size_bytes"],
                    "sha256": fingerprint["sha256"],
                }
            )
        packages.append(record)

    git_metadata = git_source_metadata(source_root, selected_relative_paths)
    pdf_fingerprint = _display_fingerprint(openstax_pdf, openstax_pdf.name)
    return {
        "schema_version": 2,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "chapters": list(selected_chapters),
            "ngram_sizes": list(ngram_sizes),
            "minimum_match_block_words": min_match_block,
        },
        "openstax": {
            **pdf_fingerprint,
            "source_url": openstax_url,
            "page_count": openstax_page_count,
            "pdf_metadata": openstax_metadata or {},
        },
        "authoring_source": {
            **git_metadata,
            "topic_package_inputs": packages,
        },
        "comparison_code": {
            "script": _display_fingerprint(
                script_path, "scripts/compare_openstax_chemillusion.py"
            ),
            "chapter_map": _display_fingerprint(
                chapter_map_path, "config/chapter_map.json"
            ),
            "molecule_aliases": _display_fingerprint(
                molecule_aliases_path, "config/molecule_aliases.csv"
            ),
        },
    }


def normalize_unicode(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    replacements = {
        "−": "-",
        "–": "-",
        "—": "-",
        "ﬁ": "fi",
        "ﬂ": "fl",
        "": "f",  # common extraction artifact in this PDF
        "": "i",
        "π": "pi",
        "σ": "sigma",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def tokenize(text: str) -> list[str]:
    text = normalize_unicode(text).casefold()
    return re.findall(r"[a-z0-9]+(?:'[a-z]+)?", text)


def parse_range_list(value: str) -> tuple[int, ...]:
    """Parse strings such as '1-26', '1,2,4-7', or '5 8 12'."""
    numbers: set[int] = set()
    for part in re.split(r"[\s,]+", value.strip()):
        if not part:
            continue
        if "-" in part:
            start_s, end_s = part.split("-", 1)
            start, end = int(start_s), int(end_s)
            if end < start:
                raise ValueError(f"Invalid descending range: {part}")
            numbers.update(range(start, end + 1))
        else:
            numbers.add(int(part))
    if not numbers:
        raise ValueError("No numeric values were supplied")
    return tuple(sorted(numbers))


def load_chapter_map(path: Path) -> dict[int, ChapterSpec]:
    data = json.loads(path.read_text(encoding="utf-8"))
    entries = data["chapters"] if isinstance(data, dict) else data
    result: dict[int, ChapterSpec] = {}
    for row in entries:
        spec = ChapterSpec(
            chapter=int(row["chapter"]),
            slug=str(row["slug"]),
            title=str(row.get("title", "")),
        )
        result[spec.chapter] = spec
    return result


def download_file(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "OpenStax-ChemIllusion-comparison/1.0"},
    )
    with urllib.request.urlopen(request) as response, destination.open("wb") as handle:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            handle.write(chunk)


def resolve_openstax_pdf(local_path: Path | None, url: str, cache_dir: Path) -> Path:
    if local_path is not None:
        if not local_path.exists():
            raise FileNotFoundError(f"OpenStax PDF not found: {local_path}")
        return local_path
    destination = cache_dir / DEFAULT_OPENSTAX_CACHE_FILENAME
    if not destination.exists() or destination.stat().st_size == 0:
        print(f"Downloading OpenStax PDF to {destination}")
        download_file(url, destination)
    return destination


def extract_pdf_pages(pdf_path: Path) -> list[str]:
    document = fitz.open(pdf_path)
    try:
        return [page.get_text("text", sort=True) for page in document]
    finally:
        document.close()


def chapter_candidate_score(page_text: str, spec: ChapterSpec) -> int:
    head = normalize_unicode(page_text[:7000])
    heading = re.search(rf"(?im)^\s*CHAPTER\s+{spec.chapter}\b", head)
    if not heading:
        return -1
    score = 0
    if heading.start() < 250:
        score += 5
    if re.search(r"CHAPTER\s+CONTENTS", head, re.I):
        score += 5
    if re.search(r"WHY\s+THIS\s+CHAPTER", head, re.I):
        score += 4
    title_tokens = [t for t in tokenize(spec.title) if len(t) > 3]
    if title_tokens:
        hits = sum(1 for token in title_tokens if token in tokenize(head[:1600]))
        score += min(hits, 4)
    return score


def locate_chapter_starts(
    pages: Sequence[str], chapter_map: dict[int, ChapterSpec]
) -> dict[int, int]:
    starts: dict[int, int] = {}
    for chapter, spec in sorted(chapter_map.items()):
        candidates: list[tuple[int, int]] = []
        for page_index, page_text in enumerate(pages):
            score = chapter_candidate_score(page_text, spec)
            if score >= 0:
                candidates.append((score, page_index))
        if not candidates:
            continue
        candidates.sort(key=lambda pair: (-pair[0], pair[1]))
        starts[chapter] = candidates[0][1]
    return starts


def extract_openstax_chapter(
    pages: Sequence[str], chapter: int, starts: dict[int, int]
) -> str:
    if chapter not in starts:
        raise ValueError(f"Could not locate OpenStax chapter {chapter}")
    start = starts[chapter]
    later_starts = [index for number, index in starts.items() if number > chapter and index > start]
    if later_starts:
        end = min(later_starts)
    else:
        end = len(pages)
        appendix_re = re.compile(r"(?im)^\s*(APPENDIX|GLOSSARY|INDEX)\b")
        for index in range(start + 1, len(pages)):
            if appendix_re.search(normalize_unicode(pages[index][:600])):
                end = index
                break
    return "\n".join(pages[start:end])


def strip_caption_paragraphs(text: str) -> str:
    return re.sub(
        r"(?ms)^\s*(?:FIGURE|TABLE)\s+\d+\.\d+\s+.*?(?=\n\s*\n)",
        "\n",
        text,
    )


def clean_openstax_expository(text: str) -> str:
    text = normalize_unicode(text)
    why = re.search(r"WHY\s+THIS\s+CHAPTER\?", text, re.I)
    if why:
        text = text[why.start() :]
    for terminal_heading in ("Key Terms", "Summary", "Additional Problems"):
        match = re.search(rf"(?im)^\s*{re.escape(terminal_heading)}\s*$", text)
        if match:
            text = text[: match.start()]
            break
    text = strip_caption_paragraphs(text)
    cleaned_lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            cleaned_lines.append("")
            continue
        if stripped == "-----":
            continue
        if stripped.startswith("Access for free at openstax.org"):
            continue
        if re.match(r"^\d+\s+\d+\s+[•·]", stripped):
            continue
        cleaned_lines.append(line)
    return re.sub(r"[ \t]+", " ", "\n".join(cleaned_lines))


def ngrams(tokens: Sequence[str], n: int) -> set[tuple[str, ...]]:
    if len(tokens) < n:
        return set()
    return {tuple(tokens[index : index + n]) for index in range(len(tokens) - n + 1)}


def textual_overlap(
    chapter: int,
    chemillusion_text: str,
    openstax_text: str,
    ngram_sizes: Sequence[int],
    min_match_block: int,
) -> tuple[list[dict[str, Any]], dict[str, Any], list[dict[str, Any]]]:
    ci_tokens = tokenize(chemillusion_text)
    os_tokens = tokenize(openstax_text)
    rows: list[dict[str, Any]] = []
    for n in ngram_sizes:
        ci_ngrams = ngrams(ci_tokens, n)
        os_ngrams = ngrams(os_tokens, n)
        common = ci_ngrams & os_ngrams
        union = ci_ngrams | os_ngrams
        rows.append(
            {
                "chapter": chapter,
                "n": n,
                "chemillusion_unique_ngrams": len(ci_ngrams),
                "openstax_unique_ngrams": len(os_ngrams),
                "common_unique_ngrams": len(common),
                "jaccard": len(common) / len(union) if union else math.nan,
                "chemillusion_ngram_coverage": (
                    len(common) / len(ci_ngrams) if ci_ngrams else math.nan
                ),
                "openstax_ngram_coverage": (
                    len(common) / len(os_ngrams) if os_ngrams else math.nan
                ),
            }
        )

    matcher = SequenceMatcher(None, ci_tokens, os_tokens, autojunk=False)
    blocks = [
        block
        for block in matcher.get_matching_blocks()
        if block.size >= min_match_block
    ]
    longest = matcher.find_longest_match(0, len(ci_tokens), 0, len(os_tokens))
    summary = {
        "chapter": chapter,
        "chemillusion_words": len(ci_tokens),
        "openstax_words": len(os_tokens),
        "longest_exact_run_words": longest.size,
        "matching_blocks_at_or_above_minimum": len(blocks),
        "minimum_match_block_words": min_match_block,
        "chemillusion_token_coverage_in_long_blocks": (
            sum(block.size for block in blocks) / len(ci_tokens)
            if ci_tokens
            else math.nan
        ),
    }
    block_rows = [
        {
            "chapter": chapter,
            "chemillusion_start_token": block.a,
            "openstax_start_token": block.b,
            "length_words": block.size,
            "phrase": " ".join(ci_tokens[block.a : block.a + block.size]),
        }
        for block in blocks
    ]
    return rows, summary, block_rows


def canonical_smiles(smiles: str) -> str | None:
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        return None
    return Chem.MolToSmiles(molecule, canonical=True, isomericSmiles=True)


def aliases_from_name(name: str) -> set[str]:
    cleaned = normalize_unicode(name).strip()
    aliases = {cleaned}
    leading_stereodescriptor = bool(
        re.match(r"^\((?:\d*[RSEZ])(?:,\d*[RSEZ])*\)", cleaned, re.I)
    )
    for match in re.finditer(r"\(([^()]+)\)", cleaned):
        alias = match.group(1).strip()
        preceded_by_word = match.start() > 0 and cleaned[match.start() - 1].isalnum()
        generic_description = bool(re.match(r"^(?:a|an|the)\s+", alias, re.I))
        stereodescriptor = bool(
            re.fullmatch(r"(?:\d*[RSEZ])(?:,\d*[RSEZ])*", alias, re.I)
        )
        if alias and not (preceded_by_word or generic_description or stereodescriptor):
            aliases.add(alias)
    without_parenthetical = re.sub(r"\s*\([^()]+\)\s*", " ", cleaned).strip()
    without_parenthetical = without_parenthetical.lstrip("-–— ")
    if without_parenthetical and not leading_stereodescriptor:
        aliases.add(without_parenthetical)
    return {alias for alias in aliases if alias}


def looks_like_identity_molecule(name: str, alt_text: str, description: str) -> bool:
    if re.match(r"^(?:a|an)\s+", normalize_unicode(name).strip(), re.I):
        return False
    folded = normalize_unicode(" ".join([name, alt_text, description])).casefold()
    for term in GENERIC_MOLECULE_ASSET_TERMS:
        pattern = r"(?<![a-z0-9])" + re.escape(term) + r"(?![a-z0-9])"
        if re.search(pattern, folded):
            return False
    return True


def load_alias_overrides(path: Path | None) -> dict[str, dict[str, Any]]:
    if path is None or not path.exists():
        return {}
    result: dict[str, dict[str, Any]] = {}
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"canonical_smiles", "preferred_name", "aliases", "include"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(
                f"Alias CSV must contain columns: {', '.join(sorted(required))}"
            )
        for row in reader:
            smiles = canonical_smiles(row["canonical_smiles"].strip())
            if not smiles:
                warn(f"Ignoring invalid alias SMILES: {row['canonical_smiles']}")
                continue
            aliases = {
                alias.strip()
                for alias in row["aliases"].split("|")
                if alias.strip()
            }
            result[smiles] = {
                "preferred_name": row["preferred_name"].strip(),
                "aliases": aliases,
                "include": row["include"].strip().casefold() not in {"false", "0", "no"},
            }
    return result


def classify_chemillusion_visual(block_type: str, content: dict[str, Any]) -> str:
    text = " ".join(
        str(content.get(key, ""))
        for key in ("name", "title", "alt_text", "description")
    ).casefold()
    if block_type == "reaction_coordinate" or any(
        term in text for term in ("energy diagram", "reaction coordinate", "delta g")
    ):
        return "energy_diagram"
    if any(term in text for term in ("curved arrow", "mechanism", "electron-pair", "reaction")):
        return "reaction_mechanism"
    if any(term in text for term in ("table", "chart", "range", "relationship", "values")):
        return "data_table"
    if any(term in text for term in ("orbital", "hybridization", "sigma", "pi bond")):
        return "atomic_orbital"
    if any(term in text for term in ("geometry", "chair", "newman", "conformation")):
        return "molecular_geometry"
    if block_type == "molecule" or content.get("smiles"):
        return "molecular_structure"
    return block_type or "other"


def parse_raw_chemillusion_chapter(data: dict[str, Any], source_path: str) -> dict[str, Any]:
    sections: list[dict[str, str]] = []
    visuals: list[dict[str, Any]] = []
    molecule_assets: list[dict[str, str]] = []

    for section in data.get("sections", []):
        section_texts: list[str] = []
        for block in section.get("blocks", []):
            if block.get("is_hidden"):
                continue
            block_type = str(block.get("block_type", ""))
            content = block.get("content") or {}
            if block_type in TEXT_BLOCK_TYPES:
                markdown = str(content.get("markdown", "")).strip()
                if markdown:
                    section_texts.append(markdown)
                continue
            if block_type in NON_VISUAL_BLOCK_TYPES or block_type == "video":
                continue

            name = str(content.get("name") or content.get("title") or block.get("id", ""))
            alt_text = str(content.get("alt_text", ""))
            description = str(content.get("description", ""))
            smiles = str(content.get("smiles", "")).strip()
            visuals.append(
                {
                    "id": str(block.get("id", "")),
                    "name": name,
                    "category": classify_chemillusion_visual(block_type, content),
                    "block_type": block_type,
                    "alt_text": alt_text,
                    "description": description,
                    "smiles": smiles,
                }
            )
            if block_type == "molecule" and smiles and looks_like_identity_molecule(
                name, alt_text, description
            ):
                molecule_assets.append(
                    {
                        "name": name,
                        "smiles": smiles,
                        "alt_text": alt_text,
                        "description": description,
                    }
                )
        sections.append(
            {
                "title": str(section.get("title", "")),
                "text": "\n\n".join(section_texts),
            }
        )

    return {
        "title": str(data.get("chapter_title", "")),
        "available": bool(data.get("available", False)),
        "source_path": source_path,
        "sections": sections,
        "figure_assets": visuals,
        "molecule_assets": molecule_assets,
    }


def load_chemillusion_from_directory(
    directory: Path,
    selected_specs: Sequence[ChapterSpec],
    strict: bool,
) -> dict[int, dict[str, Any]]:
    chapters: dict[int, dict[str, Any]] = {}
    for spec in selected_specs:
        path = directory / f"{spec.slug}.json"
        if not path.exists():
            message = f"ChemIllusion chapter file missing: {path}"
            if strict:
                raise FileNotFoundError(message)
            warn(message)
            continue
        raw = json.loads(path.read_text(encoding="utf-8"))
        chapters[spec.chapter] = parse_raw_chemillusion_chapter(raw, str(path))
    return chapters


def load_chemillusion_from_snapshot(path: Path) -> dict[int, dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    chapters: dict[int, dict[str, Any]] = {}
    for chapter_s, record in data.get("chapters", {}).items():
        chapter = int(chapter_s)
        molecule_assets = [
            asset
            for asset in record.get("figure_assets", [])
            if asset.get("smiles")
            and asset.get("include_structure_similarity", True)
            and looks_like_identity_molecule(
                str(asset.get("name", "")),
                str(asset.get("alt_text", "")),
                str(asset.get("description", "")),
            )
        ]
        chapters[chapter] = {
            **record,
            "molecule_assets": molecule_assets,
        }
    return chapters


def validate_chapter_availability(
    chapters: dict[int, dict[str, Any]], strict: bool
) -> tuple[int, ...]:
    unavailable = tuple(
        chapter
        for chapter, record in sorted(chapters.items())
        if not bool(record.get("available", False))
    )
    if unavailable:
        message = (
            "ChemIllusion selected chapters are unavailable: "
            + ", ".join(map(str, unavailable))
        )
        if strict:
            raise ValueError(message)
        warn(message)
    return unavailable


def build_molecule_records(
    chapter_data: dict[str, Any],
    alias_overrides: dict[str, dict[str, Any]],
) -> list[MoleculeRecord]:
    records: dict[str, MoleculeRecord] = {}
    for asset in chapter_data.get("molecule_assets", []):
        raw_smiles = str(asset.get("smiles", ""))
        canonical = canonical_smiles(raw_smiles)
        if not canonical:
            warn(f"Skipping invalid ChemIllusion SMILES: {raw_smiles}")
            continue
        name = str(asset.get("name", canonical)).strip()
        aliases = aliases_from_name(name)
        override = alias_overrides.get(canonical)
        if override and not override["include"]:
            continue
        preferred = (
            override["preferred_name"] if override and override["preferred_name"] else name
        )
        if override:
            aliases.update(override["aliases"])
        record = records.get(canonical)
        if record is None:
            records[canonical] = MoleculeRecord(
                canonical_smiles=canonical,
                preferred_name=preferred,
                aliases=set(aliases),
                source_names={name},
            )
        else:
            record.aliases.update(aliases)
            record.source_names.add(name)
    return list(records.values())


def alias_pattern(alias: str) -> re.Pattern[str] | None:
    normalized = normalize_unicode(alias).casefold().strip()
    if not normalized:
        return None
    compact = re.sub(r"\s+", " ", normalized)
    if len(compact) < 3 and not any(char.isdigit() for char in compact):
        return None
    escaped = re.escape(compact).replace(r"\ ", r"\s+")
    return re.compile(rf"(?<![a-z0-9]){escaped}(?![a-z0-9])", re.I)


def identical_molecule_counts(
    chapter: int,
    molecule_records: Sequence[MoleculeRecord],
    openstax_text: str,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    folded = normalize_unicode(openstax_text).casefold()
    detail_rows: list[dict[str, Any]] = []
    shared_count = 0
    for record in sorted(molecule_records, key=lambda item: item.preferred_name.casefold()):
        matched_aliases: list[str] = []
        for alias in sorted(record.aliases, key=lambda item: (-len(item), item.casefold())):
            pattern = alias_pattern(alias)
            if pattern and pattern.search(folded):
                matched_aliases.append(alias)
        is_shared = bool(matched_aliases)
        shared_count += int(is_shared)
        detail_rows.append(
            {
                "chapter": chapter,
                "preferred_name": record.preferred_name,
                "canonical_smiles": record.canonical_smiles,
                "chemillusion_source_names": " | ".join(sorted(record.source_names)),
                "aliases_checked": " | ".join(sorted(record.aliases)),
                "matched_aliases_in_openstax": " | ".join(sorted(set(matched_aliases))),
                "identical_molecule_named_in_openstax": is_shared,
            }
        )
    total = len(molecule_records)
    summary = {
        "chapter": chapter,
        "chemillusion_unique_molecules": total,
        "identical_molecules_named_in_openstax": shared_count,
        "chemillusion_molecule_overlap_fraction": shared_count / total if total else math.nan,
    }
    return summary, detail_rows


def extract_captions(text: str, chapter: int, kind: str) -> list[dict[str, str]]:
    normalized = normalize_unicode(text)
    label_re = re.compile(rf"{kind}\s+({chapter}\.\d+)\b", re.I)
    labels = sorted(
        set(label_re.findall(normalized)),
        key=lambda label: tuple(int(value) for value in label.split(".")),
    )
    rows: list[dict[str, str]] = []
    for label in labels:
        match = re.search(
            rf"{kind}\s+{re.escape(label)}\s+(.*?)"
            rf"(?=\n\s*\n|FIGURE\s+|TABLE\s+|\Z)",
            normalized,
            re.S | re.I,
        )
        caption = " ".join(match.group(1).split()) if match else ""
        rows.append({"label": label, "caption": caption})
    return rows


def classify_openstax_figure(caption: str) -> str:
    text = normalize_unicode(caption).casefold()
    if any(term in text for term in ("reaction coordinate", "energy versus", "relative energy")):
        return "energy_diagram"
    if any(term in text for term in ("curved arrow", "mechanism", "reaction of", "lewis acid", "lewis base")):
        return "reaction_mechanism"
    if any(term in text for term in ("orbital", "nucleus", "electron density", "hybridization", "molecular orbital")):
        return "atomic_orbital"
    if any(term in text for term in ("electrostatic potential", "dipole", "dispersion", "boiling point", "melting point")):
        return "molecular_property_model"
    if any(term in text for term in ("bond angle", "geometry", "chair", "newman", "conformation")):
        return "molecular_geometry"
    if any(term in text for term in ("structure of", "line-bond", "skeletal", "molecule")):
        return "molecular_structure"
    if any(term in text for term in ("enzyme", "protein", "plant", "drug", "biological")):
        return "biological_context"
    return "other"


def figure_inventory(
    chapter: int,
    openstax_raw: str,
    chemillusion_data: dict[str, Any],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for figure in extract_captions(openstax_raw, chapter, "FIGURE"):
        rows.append(
            {
                "chapter": chapter,
                "source": "OpenStax",
                "asset_id": f"Figure {figure['label']}",
                "label": figure["caption"][:240],
                "category": classify_openstax_figure(figure["caption"]),
                "asset_type": "figure",
                "text_description_present": bool(figure["caption"]),
            }
        )
    for table in extract_captions(openstax_raw, chapter, "TABLE"):
        rows.append(
            {
                "chapter": chapter,
                "source": "OpenStax",
                "asset_id": f"Table {table['label']}",
                "label": table["caption"][:240],
                "category": "data_table",
                "asset_type": "table",
                "text_description_present": bool(table["caption"]),
            }
        )
    for asset in chemillusion_data.get("figure_assets", []):
        rows.append(
            {
                "chapter": chapter,
                "source": "ChemIllusion",
                "asset_id": str(asset.get("id", "")),
                "label": str(asset.get("name", "")),
                "category": str(asset.get("category", "other")),
                "asset_type": str(asset.get("block_type", "reader_block")),
                "text_description_present": bool(asset.get("alt_text")),
            }
        )
    return rows


def save_heatmap(
    values: pd.DataFrame,
    output_path: Path,
    title: str,
    x_label: str,
    y_label: str,
    percent: bool = False,
    subtitle: str = "",
) -> None:
    if values.empty:
        return
    width = max(8.0, 0.65 * len(values.columns) + 3.5)
    height = max(4.8, 0.42 * len(values.index) + 2.8)
    figure, axis = plt.subplots(figsize=(width, height), facecolor=PLOT_BACKGROUND)
    axis.set_facecolor(PLOT_BACKGROUND)
    matrix = values.to_numpy(dtype=float)
    image = axis.imshow(
        matrix,
        aspect="auto",
        interpolation="nearest",
        cmap=HEATMAP_CMAP,
    )
    axis.set_title(title, loc="left", color=INK, fontweight="bold", pad=22)
    if subtitle:
        axis.text(
            0,
            1.005,
            subtitle,
            transform=axis.transAxes,
            ha="left",
            va="bottom",
            color=MUTED_INK,
            fontsize=9,
        )
    axis.set_xlabel(x_label)
    axis.set_ylabel(y_label)
    axis.set_xticks(range(len(values.columns)), labels=[str(value) for value in values.columns])
    axis.set_yticks(range(len(values.index)), labels=[str(value) for value in values.index])
    plt.setp(axis.get_xticklabels(), rotation=45, ha="right")
    for row_index in range(matrix.shape[0]):
        for column_index in range(matrix.shape[1]):
            value = matrix[row_index, column_index]
            if np.isnan(value):
                label = "-"
            elif percent:
                label = f"{value:.2f}%"
            else:
                label = f"{value:.0f}"
            text_color = "#FFFFFF" if not np.isnan(value) and image.norm(value) > 0.58 else INK
            axis.text(
                column_index,
                row_index,
                label,
                ha="center",
                va="center",
                fontsize=7,
                color=text_color,
            )
    colorbar = figure.colorbar(image, ax=axis)
    colorbar.outline.set_edgecolor(GRID)
    axis.tick_params(colors=INK)
    axis.xaxis.label.set_color(INK)
    axis.yaxis.label.set_color(INK)
    figure.tight_layout()
    figure.savefig(output_path, dpi=180, facecolor=PLOT_BACKGROUND)
    plt.close(figure)


def save_plot_text_overlap(df: pd.DataFrame, output_path: Path) -> None:
    pivot = (
        df.pivot(index="chapter", columns="n", values="chemillusion_ngram_coverage")
        .sort_index()
        .sort_index(axis=1)
        * 100
    )
    pivot.columns = [f"{column}-word" for column in pivot.columns]
    save_heatmap(
        pivot,
        output_path,
        "Exact phrase overlap: ChemIllusion n-grams found in OpenStax",
        "Exact phrase length",
        "Chapter",
        percent=True,
        subtitle="Percent of unique ChemIllusion n-grams also present in the OpenStax chapter",
    )


def save_plot_longest_match(df: pd.DataFrame, output_path: Path) -> None:
    if df.empty:
        return
    ordered = df.sort_values("chapter")
    figure, axis = plt.subplots(
        figsize=(max(8, 0.35 * len(ordered) + 4), 5.0),
        facecolor=PLOT_BACKGROUND,
    )
    bars = axis.bar(
        ordered["chapter"].astype(str),
        ordered["longest_exact_run_words"],
        color=BLUE,
        edgecolor=BLUE_DARK,
        linewidth=0.7,
    )
    axis.set_title(
        "Longest exact contiguous word sequence",
        loc="left",
        color=INK,
        fontweight="bold",
        pad=22,
    )
    axis.text(
        0,
        1.01,
        "Maximum exact token run per chapter; bars begin at zero",
        transform=axis.transAxes,
        color=MUTED_INK,
        fontsize=9,
    )
    axis.set_xlabel("Chapter")
    axis.set_ylabel("Words")
    axis.set_ylim(bottom=0)
    axis.bar_label(bars, fmt="%.0f", fontsize=7)
    axis.grid(axis="y", color=GRID, linewidth=0.7)
    axis.set_axisbelow(True)
    axis.spines[["top", "right"]].set_visible(False)
    figure.tight_layout()
    figure.savefig(output_path, dpi=180, facecolor=PLOT_BACKGROUND)
    plt.close(figure)


def save_plot_identical_molecules(df: pd.DataFrame, output_path: Path) -> None:
    if df.empty:
        return
    ordered = df.sort_values("chapter")
    x = np.arange(len(ordered))
    width = 0.38
    figure, axis = plt.subplots(
        figsize=(max(9, 0.5 * len(ordered) + 4), 5.8),
        facecolor=PLOT_BACKGROUND,
    )
    all_bars = axis.bar(
        x - width / 2,
        ordered["chemillusion_unique_molecules"],
        width,
        label="Unique ChemIllusion molecules",
        color=BLUE,
        edgecolor=BLUE_DARK,
        linewidth=0.7,
    )
    shared_bars = axis.bar(
        x + width / 2,
        ordered["identical_molecules_named_in_openstax"],
        width,
        label="Identical molecules named in OpenStax",
        color=GOLD,
        edgecolor=INK,
        linewidth=0.7,
        hatch="//",
    )
    axis.set_title(
        "Exact molecule identity counts",
        loc="left",
        color=INK,
        fontweight="bold",
        pad=22,
    )
    axis.text(
        0,
        1.01,
        "Canonical ChemIllusion structures and the subset supported by an OpenStax name alias",
        transform=axis.transAxes,
        color=MUTED_INK,
        fontsize=9,
    )
    axis.set_xlabel("Chapter")
    axis.set_ylabel("Unique canonical molecules")
    axis.set_xticks(x, ordered["chapter"].astype(str))
    axis.legend(frameon=False, ncol=2, loc="upper center")
    axis.set_ylim(bottom=0)
    axis.bar_label(all_bars, fmt="%.0f", fontsize=6, padding=2)
    axis.bar_label(shared_bars, fmt="%.0f", fontsize=6, padding=2)
    axis.grid(axis="y", color=GRID, linewidth=0.7)
    axis.set_axisbelow(True)
    axis.spines[["top", "right"]].set_visible(False)
    figure.tight_layout()
    figure.savefig(output_path, dpi=180, facecolor=PLOT_BACKGROUND)
    plt.close(figure)


def save_plot_figure_categories(df: pd.DataFrame, output_path: Path) -> None:
    if df.empty:
        return
    grouped = (
        df.groupby(["category", "chapter", "source"])
        .size()
        .rename("count")
        .reset_index()
    )
    grouped["column"] = grouped.apply(
        lambda row: f"Ch{int(row['chapter'])} {'OS' if row['source'] == 'OpenStax' else 'CI'}",
        axis=1,
    )
    pivot = grouped.pivot(index="category", columns="column", values="count").fillna(0)
    ordered_columns: list[str] = []
    for chapter in sorted(df["chapter"].unique()):
        ordered_columns.extend([f"Ch{int(chapter)} OS", f"Ch{int(chapter)} CI"])
    pivot = pivot.reindex(columns=[column for column in ordered_columns if column in pivot.columns])
    save_heatmap(
        pivot,
        output_path,
        "Visual asset taxonomy by chapter and source",
        "Chapter and source",
        "Visual category",
        percent=False,
        subtitle="Caption-classified OpenStax assets and block-classified ChemIllusion assets",
    )


def markdown_table(df: pd.DataFrame, columns: Sequence[str]) -> str:
    if df.empty:
        return "_No rows._"
    subset = df.loc[:, list(columns)].copy()
    return subset.to_markdown(index=False)


def write_markdown_report(
    output_path: Path,
    selected_chapters: Sequence[int],
    ngram_sizes: Sequence[int],
    min_match_block: int,
    text_summary: pd.DataFrame,
    molecule_summary: pd.DataFrame,
    figure_totals: pd.DataFrame,
    skipped: Sequence[int],
    text_ngram_metrics: pd.DataFrame | None = None,
) -> None:
    lines = [
        "# OpenStax–ChemIllusion full-book comparison results",
        "",
        f"Requested chapters: {', '.join(map(str, selected_chapters))}",
        f"Exact phrase lengths: {', '.join(map(str, ngram_sizes))} words",
        f"Minimum contiguous match block: {min_match_block} words",
        "",
    ]
    if text_ngram_metrics is not None and not text_ngram_metrics.empty:
        phrase_summary = (
            text_ngram_metrics.groupby("n", as_index=False)[
                ["chemillusion_unique_ngrams", "common_unique_ngrams"]
            ]
            .sum()
            .sort_values("n")
        )
        phrase_summary["weighted_chemillusion_coverage"] = phrase_summary.apply(
            lambda row: (
                row["common_unique_ngrams"] / row["chemillusion_unique_ngrams"]
                if row["chemillusion_unique_ngrams"]
                else math.nan
            ),
            axis=1,
        )
        first = phrase_summary.iloc[0]
        phrase_table = phrase_summary.copy()
        phrase_table["weighted_chemillusion_coverage"] = phrase_table[
            "weighted_chemillusion_coverage"
        ].map(lambda value: f"{value:.2%}" if not math.isnan(value) else "-")
        lines.extend(
            [
                "## Full-book quantitative summary",
                "",
                (
                    f"Across chapter-local unique {int(first['n'])}-word n-grams, "
                    f"{int(first['common_unique_ngrams']):,} of "
                    f"{int(first['chemillusion_unique_ngrams']):,} matched "
                    f"({first['weighted_chemillusion_coverage']:.2%})."
                ),
                "",
                markdown_table(
                    phrase_table,
                    [
                        "n",
                        "chemillusion_unique_ngrams",
                        "common_unique_ngrams",
                        "weighted_chemillusion_coverage",
                    ],
                ),
                "",
            ]
        )
        if not text_summary.empty:
            longest = text_summary.loc[
                text_summary["longest_exact_run_words"].idxmax()
            ]
            lines.extend(
                [
                    f"The longest exact contiguous run was {int(longest['longest_exact_run_words'])} words in Chapter {int(longest['chapter'])}.",
                    "",
                ]
            )
        if not molecule_summary.empty:
            molecule_total = int(
                molecule_summary["chemillusion_unique_molecules"].sum()
            )
            shared_total = int(
                molecule_summary["identical_molecules_named_in_openstax"].sum()
            )
            molecule_fraction = shared_total / molecule_total if molecule_total else math.nan
            lines.extend(
                [
                    (
                        f"Name-supported exact identity was found for {shared_total:,} of "
                        f"{molecule_total:,} chapter-local canonical ChemIllusion molecule records "
                        f"({molecule_fraction:.2%})."
                    ),
                    "",
                ]
            )
        if not figure_totals.empty:
            source_totals = (
                figure_totals.groupby("source")["visual_asset_count"].sum().to_dict()
            )
            lines.extend(
                [
                    (
                        "The inventory contains "
                        f"{int(source_totals.get('OpenStax', 0)):,} OpenStax and "
                        f"{int(source_totals.get('ChemIllusion', 0)):,} ChemIllusion visual assets."
                    ),
                    "",
                ]
            )

    lines.extend(
        [
            "## Text overlap",
            "",
            markdown_table(
                text_summary,
                [
                    "chapter",
                    "chemillusion_words",
                    "openstax_words",
                    "longest_exact_run_words",
                    "matching_blocks_at_or_above_minimum",
                ],
            ),
            "",
            "![Exact phrase overlap](text_overlap_ngram_coverage.png)",
            "",
            "![Longest exact run](text_longest_exact_run.png)",
            "",
            "## Identical molecule counts",
            "",
            markdown_table(
                molecule_summary,
                [
                    "chapter",
                    "chemillusion_unique_molecules",
                    "identical_molecules_named_in_openstax",
                    "chemillusion_molecule_overlap_fraction",
                ],
            ),
            "",
            "![Identical molecule counts](identical_molecule_counts.png)",
            "",
            "## Visual asset counts",
            "",
            markdown_table(
                figure_totals,
                ["chapter", "source", "visual_asset_count"],
            ),
            "",
            "![Figure categories](figure_category_counts.png)",
            "",
            "## Reproducibility",
            "",
            "See [`run_manifest.json`](run_manifest.json) for selected-input fingerprints, public-safe source provenance, parameters, and code/configuration hashes.",
            "",
            "## Interpretation limits",
            "",
            "- Exact phrase overlap measures wording, not conceptual coverage.",
            "- Molecule identity is inferred only when an alias for an exact canonical ChemIllusion molecule appears in OpenStax text. It is not optical structure recognition.",
            "- OpenStax figure categories are inferred from extracted captions; ChemIllusion categories are inferred from reader block types and metadata.",
            "- No fingerprint similarity, Tanimoto score, perceptual image similarity, or visual-density metric is produced.",
        ]
    )
    if skipped:
        lines.extend(
            [
                "",
                "## Skipped chapters",
                "",
                ", ".join(map(str, skipped)),
            ]
        )
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _env_path(name: str) -> Path | None:
    value = os.environ.get(name, "").strip()
    return Path(value).expanduser() if value else None


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    if load_dotenv is not None:
        load_dotenv(project_root / ".env")

    default_openstax_url = os.environ.get("OPENSTAX_URL", DEFAULT_OPENSTAX_URL).strip() or DEFAULT_OPENSTAX_URL
    default_openstax_pdf = _env_path("OPENSTAX_PDF")
    default_chemillusion_root = _env_path("CHEMILLUSION_ROOT")
    default_chemillusion_dir = _env_path("CHEMILLUSION_DIR")
    default_chemillusion_provenance_root = _env_path(
        "CHEMILLUSION_PROVENANCE_ROOT"
    )

    parser = argparse.ArgumentParser(
        description="Compare OpenStax Organic Chemistry with ChemIllusion across selected chapters."
    )
    parser.add_argument("--openstax-pdf", type=Path, default=default_openstax_pdf)
    parser.add_argument("--openstax-url", default=default_openstax_url)
    parser.add_argument("--cache-dir", type=Path, default=project_root / "data" / "cache")
    parser.add_argument("--chemillusion-root", type=Path, default=default_chemillusion_root)
    parser.add_argument("--chemillusion-dir", type=Path, default=default_chemillusion_dir)
    parser.add_argument(
        "--chemillusion-provenance-root",
        type=Path,
        default=default_chemillusion_provenance_root,
        help=(
            "Original ChemIllusion checkout used for git and canonical package "
            "fingerprints when --chemillusion-root points to an isolated compile."
        ),
    )
    parser.add_argument("--chemillusion-snapshot", type=Path)
    parser.add_argument(
        "--chapter-map",
        type=Path,
        default=project_root / "config" / "chapter_map.json",
    )
    parser.add_argument(
        "--molecule-aliases",
        type=Path,
        default=project_root / "config" / "molecule_aliases.csv",
    )
    parser.add_argument("--chapters", default="1-31")
    parser.add_argument("--ngram-sizes", default="5,8,12,16,20")
    parser.add_argument("--min-match-block", type=int, default=DEFAULT_MIN_MATCH_BLOCK)
    parser.add_argument("--output-dir", type=Path, default=project_root / "outputs")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    selected_chapters = parse_range_list(args.chapters)
    ngram_sizes = parse_range_list(args.ngram_sizes)
    if any(value < 1 for value in ngram_sizes):
        parser.error("All n-gram sizes must be positive")
    if args.min_match_block < 1:
        parser.error("--min-match-block must be positive")

    chapter_map = load_chapter_map(args.chapter_map)
    unknown = [chapter for chapter in selected_chapters if chapter not in chapter_map]
    if unknown:
        parser.error(f"Chapters missing from map: {unknown}")
    selected_specs = [chapter_map[chapter] for chapter in selected_chapters]

    if args.chemillusion_snapshot:
        chemillusion_chapters = load_chemillusion_from_snapshot(args.chemillusion_snapshot)
    else:
        if args.chemillusion_dir:
            chemillusion_dir = args.chemillusion_dir
        elif args.chemillusion_root:
            chemillusion_dir = (
                args.chemillusion_root
                / "frontend"
                / "public"
                / "reader"
                / "topic-chapters"
            )
        else:
            parser.error(
                "Supply --chemillusion-root, --chemillusion-dir, or --chemillusion-snapshot"
            )
        chemillusion_chapters = load_chemillusion_from_directory(
            chemillusion_dir, selected_specs, args.strict
        )
    validate_chapter_availability(chemillusion_chapters, args.strict)

    openstax_pdf = resolve_openstax_pdf(
        args.openstax_pdf, args.openstax_url, args.cache_dir
    )
    pages = extract_pdf_pages(openstax_pdf)
    starts = locate_chapter_starts(pages, chapter_map)
    alias_overrides = load_alias_overrides(args.molecule_aliases)

    provenance_root = args.chemillusion_provenance_root or args.chemillusion_root
    if args.chemillusion_root:
        compiled_input_root = args.chemillusion_root
    elif args.chemillusion_dir:
        compiled_input_root = args.chemillusion_dir
    elif args.chemillusion_snapshot:
        compiled_input_root = args.chemillusion_snapshot.parent
    else:  # pragma: no cover - argparse/source resolution already rejects this
        compiled_input_root = None

    with fitz.open(openstax_pdf) as document:
        openstax_metadata = {
            key: value for key, value in document.metadata.items() if value
        }
    run_manifest = build_run_manifest(
        openstax_pdf=openstax_pdf,
        openstax_url=args.openstax_url,
        openstax_page_count=len(pages),
        chemillusion_root=compiled_input_root,
        chemillusion_provenance_root=provenance_root,
        selected_specs=selected_specs,
        selected_chapters=selected_chapters,
        ngram_sizes=ngram_sizes,
        min_match_block=args.min_match_block,
        script_path=Path(__file__),
        chapter_map_path=args.chapter_map,
        molecule_aliases_path=args.molecule_aliases,
        command=[Path(sys.executable).name, *sys.argv],
        openstax_metadata=openstax_metadata,
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    text_ngram_rows: list[dict[str, Any]] = []
    text_summary_rows: list[dict[str, Any]] = []
    text_block_rows: list[dict[str, Any]] = []
    molecule_summary_rows: list[dict[str, Any]] = []
    molecule_detail_rows: list[dict[str, Any]] = []
    figure_rows: list[dict[str, Any]] = []
    chapter_source_rows: list[dict[str, Any]] = []
    skipped: list[int] = []

    for chapter in selected_chapters:
        if chapter not in chemillusion_chapters:
            skipped.append(chapter)
            continue
        if chapter not in starts:
            message = f"OpenStax chapter {chapter} was not found in the PDF"
            if args.strict:
                raise ValueError(message)
            warn(message)
            skipped.append(chapter)
            continue

        ci_data = chemillusion_chapters[chapter]
        openstax_raw = extract_openstax_chapter(pages, chapter, starts)
        openstax_clean = clean_openstax_expository(openstax_raw)
        chemillusion_text = "\n\n".join(
            section.get("text", "") for section in ci_data.get("sections", [])
        )

        ngram_rows, text_summary, block_rows = textual_overlap(
            chapter,
            chemillusion_text,
            openstax_clean,
            ngram_sizes,
            args.min_match_block,
        )
        text_ngram_rows.extend(ngram_rows)
        text_summary_rows.append(text_summary)
        text_block_rows.extend(block_rows)

        molecules = build_molecule_records(ci_data, alias_overrides)
        molecule_summary, molecule_details = identical_molecule_counts(
            chapter, molecules, openstax_raw
        )
        molecule_summary_rows.append(molecule_summary)
        molecule_detail_rows.extend(molecule_details)

        figure_rows.extend(figure_inventory(chapter, openstax_raw, ci_data))
        chapter_source_rows.append(
            chapter_source_manifest_record(
                chapter=chapter,
                spec=chapter_map[chapter],
                compiled_chapter=ci_data,
            )
        )

    text_ngram_df = pd.DataFrame(text_ngram_rows)
    text_summary_df = pd.DataFrame(text_summary_rows)
    text_blocks_df = pd.DataFrame(text_block_rows)
    molecule_summary_df = pd.DataFrame(molecule_summary_rows)
    molecule_details_df = pd.DataFrame(molecule_detail_rows)
    figures_df = pd.DataFrame(figure_rows)
    chapter_sources_df = pd.DataFrame(chapter_source_rows)

    text_ngram_df.to_csv(args.output_dir / "text_overlap_ngram_metrics.csv", index=False)
    text_summary_df.to_csv(args.output_dir / "text_overlap_summary.csv", index=False)
    text_blocks_df.to_csv(args.output_dir / "text_exact_match_blocks.csv", index=False)
    molecule_summary_df.to_csv(args.output_dir / "identical_molecule_summary.csv", index=False)
    molecule_details_df.to_csv(args.output_dir / "identical_molecule_details.csv", index=False)
    figures_df.to_csv(args.output_dir / "figure_asset_inventory.csv", index=False)
    chapter_sources_df.to_csv(args.output_dir / "chapter_source_manifest.csv", index=False)

    if not figures_df.empty:
        figure_totals_df = (
            figures_df.groupby(["chapter", "source"])
            .size()
            .rename("visual_asset_count")
            .reset_index()
        )
        figure_category_df = (
            figures_df.groupby(["chapter", "source", "category"])
            .size()
            .rename("count")
            .reset_index()
        )
    else:
        figure_totals_df = pd.DataFrame(
            columns=["chapter", "source", "visual_asset_count"]
        )
        figure_category_df = pd.DataFrame(
            columns=["chapter", "source", "category", "count"]
        )
    figure_totals_df.to_csv(args.output_dir / "figure_total_counts.csv", index=False)
    figure_category_df.to_csv(args.output_dir / "figure_category_counts.csv", index=False)

    save_plot_text_overlap(
        text_ngram_df, args.output_dir / "text_overlap_ngram_coverage.png"
    )
    save_plot_longest_match(
        text_summary_df, args.output_dir / "text_longest_exact_run.png"
    )
    save_plot_identical_molecules(
        molecule_summary_df, args.output_dir / "identical_molecule_counts.png"
    )
    save_plot_figure_categories(
        figures_df, args.output_dir / "figure_category_counts.png"
    )

    summary = {
        "requested_chapters": list(selected_chapters),
        "completed_chapters": sorted(text_summary_df["chapter"].tolist())
        if not text_summary_df.empty
        else [],
        "skipped_chapters": skipped,
        "ngram_sizes": list(ngram_sizes),
        "minimum_match_block_words": args.min_match_block,
        "outputs": {
            "text_overlap_plot": "text_overlap_ngram_coverage.png",
            "longest_match_plot": "text_longest_exact_run.png",
            "identical_molecule_plot": "identical_molecule_counts.png",
            "figure_category_plot": "figure_category_counts.png",
            "run_manifest": "run_manifest.json",
        },
        "excluded_methods": [
            "Tanimoto or fingerprint similarity",
            "visual asset density",
            "perceptual image similarity",
        ],
    }
    (args.output_dir / "results_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    (args.output_dir / "run_manifest.json").write_text(
        json.dumps(run_manifest, indent=2) + "\n", encoding="utf-8"
    )
    write_markdown_report(
        args.output_dir / "RESULTS.md",
        selected_chapters,
        ngram_sizes,
        args.min_match_block,
        text_summary_df,
        molecule_summary_df,
        figure_totals_df,
        skipped,
        text_ngram_metrics=text_ngram_df,
    )

    print(f"Completed {len(text_summary_df)} chapter comparisons")
    if skipped:
        print(f"Skipped chapters: {', '.join(map(str, skipped))}")
    print(f"Outputs written to: {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
