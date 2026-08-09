from __future__ import annotations

import json
import os
import runpy
import subprocess
import tempfile
import unittest
from pathlib import Path

import matplotlib
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", "/tmp/textbook-authoring-mpl")
COMPARISON = runpy.run_path(str(REPO_ROOT / "scripts/compare_openstax_chemillusion.py"))


class FullBookDefaultsTests(unittest.TestCase):
    def test_comparison_uses_a_noninteractive_plot_backend(self) -> None:
        self.assertEqual(matplotlib.get_backend().casefold(), "agg")

    def test_defaults_and_chapter_map_cover_all_31_mcmurry_chapters(self) -> None:
        chapter_map = COMPARISON["load_chapter_map"](REPO_ROOT / "config/chapter_map.json")

        self.assertEqual(COMPARISON["DEFAULT_CHAPTERS"], tuple(range(1, 32)))
        self.assertEqual(COMPARISON["DEFAULT_NGRAM_SIZES"], (5, 8, 12, 16, 20))
        self.assertEqual(
            COMPARISON["DEFAULT_OPENSTAX_URL"],
            "https://assets.openstax.org/oscms-prodcms/media/documents/"
            "organic-chemistry_-_WEB.pdf",
        )
        self.assertEqual(
            COMPARISON["DEFAULT_OPENSTAX_CACHE_FILENAME"],
            "openstax-organic-chemistry-current.pdf",
        )
        self.assertEqual(sorted(chapter_map), list(range(1, 32)))
        self.assertEqual(chapter_map[27].slug, "biomolecules-lipids")
        self.assertEqual(chapter_map[31].slug, "synthetic-polymers")

    def test_strict_run_rejects_an_unavailable_selected_chapter(self) -> None:
        with self.assertRaisesRegex(ValueError, "unavailable.*2"):
            COMPARISON["validate_chapter_availability"](
                {1: {"available": True}, 2: {"available": False}}, strict=True
            )


class TextOverlapRegressionTests(unittest.TestCase):
    def test_extra_reference_text_can_inflate_chemillusion_coverage(self) -> None:
        textual_overlap = COMPARISON["textual_overlap"]
        chemillusion = "alpha beta gamma delta epsilon zeta"
        base_reference = "alpha beta unrelated words only"
        expanded_reference = base_reference + " alpha beta gamma delta epsilon zeta"

        base_rows, _, _ = textual_overlap(1, chemillusion, base_reference, [3], 3)
        expanded_rows, _, _ = textual_overlap(1, chemillusion, expanded_reference, [3], 3)

        self.assertGreaterEqual(
            expanded_rows[0]["chemillusion_ngram_coverage"],
            base_rows[0]["chemillusion_ngram_coverage"],
        )
        self.assertGreater(
            expanded_rows[0]["chemillusion_ngram_coverage"],
            base_rows[0]["chemillusion_ngram_coverage"],
        )
        self.assertNotEqual(expanded_rows[0]["jaccard"], base_rows[0]["jaccard"])


class MoleculeAliasRegressionTests(unittest.TestCase):
    def test_parenthetical_aliases_exclude_descriptions_stereochemistry_and_polymers(self) -> None:
        aliases_from_name = COMPARISON["aliases_from_name"]

        self.assertNotIn("a ketone", aliases_from_name("Acetone (a ketone)"))
        self.assertNotIn("R,R", aliases_from_name("(R,R)-Tartaric acid"))
        self.assertNotIn("Tartaric acid", aliases_from_name("(R,R)-Tartaric acid"))
        self.assertNotIn("2E,4E", aliases_from_name("(2E,4E)-Hexa-2,4-diene"))
        self.assertNotIn("Hexa-2,4-diene", aliases_from_name("(2E,4E)-Hexa-2,4-diene"))
        self.assertNotIn(
            "ethylene terephthalate",
            aliases_from_name(
                "Terephthalic acid, the diacid of poly(ethylene terephthalate)"
            ),
        )

    def test_parenthetical_aliases_keep_chemical_names_and_abbreviations(self) -> None:
        aliases_from_name = COMPARISON["aliases_from_name"]

        self.assertIn("DMSO", aliases_from_name("Dimethyl sulfoxide (DMSO)"))
        self.assertIn("cholecalciferol", aliases_from_name("Vitamin D3 (cholecalciferol)"))

    def test_indefinite_example_labels_are_not_exact_molecule_identity(self) -> None:
        looks_like_identity_molecule = COMPARISON["looks_like_identity_molecule"]

        self.assertFalse(
            looks_like_identity_molecule(
                "A diisocyanate",
                "Hexane-1,6-diisocyanate with an isocyanate group at each end.",
                "An example used to introduce the functional group.",
            )
        )
        self.assertFalse(
            looks_like_identity_molecule(
                "A tert-butyldimethylsilyl (TBS) ether", "", ""
            )
        )


class ProvenanceTests(unittest.TestCase):
    def test_git_metadata_preserves_first_status_path_exactly(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            hidden = root / ".authored-state"
            hidden.write_text("original\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(root), "add", ".authored-state"], check=True)
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(root),
                    "-c",
                    "user.name=Comparison Test",
                    "-c",
                    "user.email=comparison@example.test",
                    "commit",
                    "-q",
                    "-m",
                    "fixture",
                ],
                check=True,
            )
            hidden.write_text("modified\n", encoding="utf-8")

            metadata = COMPARISON["git_source_metadata"](root)

        self.assertEqual(metadata["dirty_paths"], [".authored-state"])

    def test_sha256_file_returns_auditable_fingerprint(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.txt"
            source.write_bytes(b"ChemIllusion\n")

            fingerprint = COMPARISON["file_fingerprint"](source)

        self.assertEqual(fingerprint["size_bytes"], 13)
        self.assertEqual(
            fingerprint["sha256"],
            "9f0386203cd505b56348a02675d7debc8703a90085a853d59a024f24db7ade15",
        )
        self.assertEqual(fingerprint["path"], str(source.resolve()))

    def test_run_manifest_records_inputs_parameters_and_package_hashes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            compiled_root = root / "compiled"
            provenance_root = root / "provenance"
            pdf = root / "book.pdf"
            script = root / "compare.py"
            chapter_map = root / "chapter_map.json"
            aliases = root / "aliases.csv"
            package = (
                compiled_root
                / "content/organic/topic-packages/chapter-one/topic.package.json"
            )
            live_package = (
                provenance_root
                / "content/organic/topic-packages/chapter-one/topic.package.json"
            )
            for path, content in (
                (pdf, b"pdf"),
                (script, b"script"),
                (chapter_map, b"{}"),
                (aliases, b"a,b\n"),
                (package, b"{\"topic_id\": \"chapter-one\"}"),
                (live_package, b"{\"topic_id\": \"newer-live-change\"}"),
            ):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
            expected_package_sha256 = COMPARISON["file_fingerprint"](package)["sha256"]

            manifest = COMPARISON["build_run_manifest"](
                openstax_pdf=pdf,
                openstax_url="https://example.test/book.pdf",
                openstax_page_count=1245,
                chemillusion_root=compiled_root,
                chemillusion_provenance_root=provenance_root,
                selected_specs=[COMPARISON["ChapterSpec"](1, "chapter-one", "Chapter One")],
                selected_chapters=(1,),
                ngram_sizes=(5, 8),
                min_match_block=8,
                script_path=script,
                chapter_map_path=chapter_map,
                molecule_aliases_path=aliases,
                command=["compare.py", "--strict"],
            )

        self.assertEqual(manifest["schema_version"], 1)
        self.assertEqual(manifest["openstax"]["page_count"], 1245)
        self.assertEqual(manifest["parameters"]["chapters"], [1])
        self.assertEqual(manifest["parameters"]["ngram_sizes"], [5, 8])
        self.assertEqual(manifest["chemillusion"]["topic_packages"][0]["slug"], "chapter-one")
        self.assertEqual(
            manifest["chemillusion"]["topic_packages"][0]["sha256"],
            expected_package_sha256,
        )
        self.assertIn("sha256", manifest["comparison_code"]["script"])


class ReportTests(unittest.TestCase):
    def test_report_summarizes_weighted_book_level_phrase_coverage(self) -> None:
        text_ngram_metrics = pd.DataFrame(
            [
                {
                    "chapter": 1,
                    "n": 5,
                    "chemillusion_unique_ngrams": 10,
                    "openstax_unique_ngrams": 100,
                    "common_unique_ngrams": 2,
                    "jaccard": 0.02,
                    "chemillusion_ngram_coverage": 0.2,
                    "openstax_ngram_coverage": 0.02,
                }
            ]
        )
        text_summary = pd.DataFrame(
            [
                {
                    "chapter": 1,
                    "chemillusion_words": 100,
                    "openstax_words": 1000,
                    "longest_exact_run_words": 7,
                    "matching_blocks_at_or_above_minimum": 0,
                }
            ]
        )
        molecule_summary = pd.DataFrame(
            [
                {
                    "chapter": 1,
                    "chemillusion_unique_molecules": 2,
                    "identical_molecules_named_in_openstax": 1,
                    "chemillusion_molecule_overlap_fraction": 0.5,
                }
            ]
        )
        figure_totals = pd.DataFrame(
            [{"chapter": 1, "source": "OpenStax", "visual_asset_count": 3}]
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "RESULTS.md"
            COMPARISON["write_markdown_report"](
                output,
                (1,),
                (5,),
                8,
                text_summary,
                molecule_summary,
                figure_totals,
                (),
                text_ngram_metrics=text_ngram_metrics,
            )
            report = output.read_text(encoding="utf-8")

        self.assertIn("Full-book quantitative summary", report)
        self.assertIn(
            "Across chapter-local unique 5-word n-grams, 2 of 10 matched (20.00%).",
            report,
        )

    def test_report_links_every_plot_and_the_run_manifest(self) -> None:
        text_summary = pd.DataFrame(
            [
                {
                    "chapter": 1,
                    "chemillusion_words": 100,
                    "openstax_words": 1000,
                    "longest_exact_run_words": 7,
                    "matching_blocks_at_or_above_minimum": 0,
                }
            ]
        )
        molecule_summary = pd.DataFrame(
            [
                {
                    "chapter": 1,
                    "chemillusion_unique_molecules": 2,
                    "identical_molecules_named_in_openstax": 1,
                    "chemillusion_molecule_overlap_fraction": 0.5,
                }
            ]
        )
        figure_totals = pd.DataFrame(
            [{"chapter": 1, "source": "OpenStax", "visual_asset_count": 3}]
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "RESULTS.md"
            COMPARISON["write_markdown_report"](
                output,
                (1,),
                (5, 8),
                8,
                text_summary,
                molecule_summary,
                figure_totals,
                (),
            )
            report = output.read_text(encoding="utf-8")

        for expected in (
            "text_overlap_ngram_coverage.png",
            "text_longest_exact_run.png",
            "identical_molecule_counts.png",
            "figure_category_counts.png",
            "run_manifest.json",
        ):
            self.assertIn(expected, report)


if __name__ == "__main__":
    unittest.main()
