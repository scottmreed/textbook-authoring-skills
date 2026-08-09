#!/usr/bin/env python3
"""Validate persona findings or a synthesized chapter-review report.

Pure standard library (no jsonschema dependency) so it runs anywhere. The
orchestrator (review-organic-chapter skill) calls this on each of the four
persona returns before synthesis and on the synthesized report before it is
published. A persona return that fails is re-requested once, then recorded as an
open_question if it still fails.

Usage:
    python validate_findings.py <persona.json>          # validate a file
    python validate_findings.py --synthesized <report>  # validate final report
    python validate_findings.py --selftest              # run built-in checks
    cat persona.json | python validate_findings.py -    # validate stdin

Exit code 0 = valid, 1 = invalid (reasons printed to stderr), 2 = bad usage.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime

PERSONAS = {
    "Organic Chemistry Instructor",
    "Struggling Student",
    "Accessibility Persona",
    "Learner with Visual Preference",
}

SEVERITIES = {"blocker", "high", "medium", "low"}

CATEGORIES = {
    "chemical-accuracy", "notation-consistency", "sequencing",
    "conceptual-support", "objective-alignment", "misconception",
    "missing-example", "assessment-readiness", "cognitive-load",
    "worked-example-gap", "retrieval-practice", "media-equivalence",
    "alt-text-quality", "keyboard-operability", "color-motion-only",
    "interactive-fallback", "figure-accuracy", "figure-purpose",
    "visual-opportunity", "visual-redundancy",
}

LOCATION_ANCHORS = (
    "section_id", "concept_slug", "nugget_id", "asset_id",
    "question_slug", "anchor_text",
)

ENVELOPE_REQUIRED = (
    "persona", "chapter_id", "summary", "overall_score",
    "publication_blockers", "findings",
)

FINDING_REQUIRED = (
    "finding_id", "location", "severity", "category",
    "observation", "learner_impact", "recommended_outcome",
)

READINESS = {"ready", "ready with minor revisions", "major revision", "blocked"}

INTERVENTIONS = {
    "sufficient-alt-text", "longer-description",
    "structured-chemical-description", "static-image-sequence",
    "animation-or-interactive", "transcript", "keyboard-alternative",
    "text-equivalent", "alternate-activity", "prose-edit", "new-figure",
    "added-practice", "instructor-note",
}

TARGET_SURFACES = {
    "prose", "figure", "interactive", "practice", "assessment",
    "instructor-support",
}

REPORT_REQUIRED = (
    "chapter_id", "chapter_version", "run_at", "personas",
    "publication_readiness", "executive_summary", "consensus_strengths",
    "ranked_recommendations", "accessibility_blockers",
    "visual_opportunities", "sufficient_as_is", "disagreements", "regression",
)


def validate(blob: dict) -> list[str]:
    """Return a list of problems; empty means valid."""
    problems: list[str] = []

    if not isinstance(blob, dict):
        return ["top-level value is not a JSON object"]

    for key in ENVELOPE_REQUIRED:
        if key not in blob:
            problems.append(f"missing envelope key: {key}")

    persona = blob.get("persona")
    if persona is not None and persona not in PERSONAS:
        problems.append(f"unknown persona: {persona!r} (must be one of {sorted(PERSONAS)})")

    score = blob.get("overall_score")
    if score is not None and not (isinstance(score, (int, float)) and 0 <= score <= 10):
        problems.append(f"overall_score must be a number in [0, 10], got {score!r}")

    blockers = blob.get("publication_blockers")
    if blockers is not None and not isinstance(blockers, list):
        problems.append("publication_blockers must be a list of finding_ids")

    findings = blob.get("findings")
    finding_ids: set[str] = set()
    if not isinstance(findings, list):
        problems.append("findings must be a list")
    else:
        for i, finding in enumerate(findings):
            problems.extend(_validate_finding(i, finding, finding_ids))

    # Every declared blocker must reference a real finding.
    if isinstance(blockers, list):
        for fid in blockers:
            if fid not in finding_ids:
                problems.append(f"publication_blocker {fid!r} has no matching finding_id")

    return problems


def _validate_finding(index: int, finding: object, seen_ids: set[str]) -> list[str]:
    where = f"findings[{index}]"
    problems: list[str] = []
    if not isinstance(finding, dict):
        return [f"{where} is not an object"]

    for key in FINDING_REQUIRED:
        if key not in finding:
            problems.append(f"{where}: missing key {key}")

    fid = finding.get("finding_id")
    if isinstance(fid, str) and fid:
        if fid in seen_ids:
            problems.append(f"{where}: duplicate finding_id {fid!r}")
        seen_ids.add(fid)
    elif "finding_id" in finding:
        problems.append(f"{where}: finding_id must be a non-empty string")

    severity = finding.get("severity")
    if severity is not None and severity not in SEVERITIES:
        problems.append(f"{where}: severity {severity!r} not in {sorted(SEVERITIES)}")

    category = finding.get("category")
    if category is not None and category not in CATEGORIES:
        problems.append(
            f"{where}: category {category!r} not a known id "
            "(coin one only if none fit, and note it in open_questions)"
        )

    location = finding.get("location")
    if not isinstance(location, dict):
        problems.append(f"{where}: location must be an object")
    elif not any(str(location.get(a) or "").strip() for a in LOCATION_ANCHORS):
        problems.append(
            f"{where}: location has no resolvable anchor "
            f"(one of {list(LOCATION_ANCHORS)} required)"
        )

    confidence = finding.get("confidence")
    if confidence is not None and not (isinstance(confidence, (int, float)) and 0 <= confidence <= 1):
        problems.append(f"{where}: confidence must be in [0, 1], got {confidence!r}")

    return problems


def validate_synthesized_report(blob: dict) -> list[str]:
    """Return synthesized-report problems; empty means valid."""
    if not isinstance(blob, dict):
        return ["top-level value is not a JSON object"]

    problems: list[str] = []
    for key in REPORT_REQUIRED:
        if key not in blob:
            problems.append(f"missing report key: {key}")

    for key in ("chapter_id", "chapter_version", "executive_summary"):
        if key in blob and not _nonempty_string(blob[key]):
            problems.append(f"{key} must be a non-empty string")

    run_at = blob.get("run_at")
    if run_at is not None:
        try:
            datetime.fromisoformat(str(run_at).replace("Z", "+00:00"))
        except ValueError:
            problems.append(f"run_at must be ISO-8601, got {run_at!r}")

    readiness = blob.get("publication_readiness")
    if readiness is not None and readiness not in READINESS:
        problems.append(
            f"publication_readiness {readiness!r} not in {sorted(READINESS)}"
        )

    personas = blob.get("personas")
    all_finding_ids: set[str] = set()
    blocker_ids: set[str] = set()
    seen_personas: set[str] = set()
    if not isinstance(personas, list):
        problems.append("personas must be a list")
    else:
        if len(personas) != len(PERSONAS):
            problems.append(f"personas must contain exactly {len(PERSONAS)} envelopes")
        for index, persona in enumerate(personas):
            persona_problems = validate(persona)
            problems.extend(f"personas[{index}]: {problem}" for problem in persona_problems)
            if isinstance(persona, dict):
                name = persona.get("persona")
                if isinstance(name, str):
                    if name in seen_personas:
                        problems.append(f"personas[{index}]: duplicate persona {name!r}")
                    seen_personas.add(name)
                for finding in persona.get("findings", []):
                    if isinstance(finding, dict) and _nonempty_string(
                        finding.get("finding_id")
                    ):
                        all_finding_ids.add(finding["finding_id"])
                        if finding.get("severity") == "blocker":
                            blocker_ids.add(finding["finding_id"])
                blockers = persona.get("publication_blockers", [])
                if isinstance(blockers, list):
                    blocker_ids.update(fid for fid in blockers if isinstance(fid, str))
        if seen_personas != PERSONAS:
            problems.append(
                f"personas must cover exactly {sorted(PERSONAS)}, got "
                f"{sorted(seen_personas)}"
            )

    orchestrator_findings = blob.get("orchestrator_findings", [])
    if not isinstance(orchestrator_findings, list):
        problems.append("orchestrator_findings must be a list when present")
    else:
        seen_orchestrator_ids: set[str] = set()
        for index, finding in enumerate(orchestrator_findings):
            finding_problems = _validate_finding(
                index, finding, seen_orchestrator_ids
            )
            problems.extend(
                f"orchestrator_findings[{index}]: {problem}"
                for problem in finding_problems
            )
        overlap = all_finding_ids & seen_orchestrator_ids
        if overlap:
            problems.append(f"duplicate finding_ids across sources: {sorted(overlap)}")
        all_finding_ids.update(seen_orchestrator_ids)
        blocker_ids.update(
            finding["finding_id"]
            for finding in orchestrator_findings
            if isinstance(finding, dict)
            and finding.get("severity") == "blocker"
            and _nonempty_string(finding.get("finding_id"))
        )

    recommendations = blob.get("ranked_recommendations")
    if not isinstance(recommendations, list):
        problems.append("ranked_recommendations must be a list")
    else:
        seen_rec_ids: set[str] = set()
        for index, recommendation in enumerate(recommendations):
            problems.extend(
                _validate_recommendation(
                    index, recommendation, seen_rec_ids, all_finding_ids
                )
            )

    for key in (
        "consensus_strengths", "accessibility_blockers",
        "visual_opportunities", "sufficient_as_is",
    ):
        value = blob.get(key)
        if value is not None and not isinstance(value, list):
            problems.append(f"{key} must be a list")

    access_blockers = blob.get("accessibility_blockers")
    if isinstance(access_blockers, list):
        for fid in access_blockers:
            if fid not in all_finding_ids:
                problems.append(
                    f"accessibility_blocker {fid!r} has no matching finding_id"
                )

    disagreements = blob.get("disagreements")
    if disagreements is not None and not isinstance(disagreements, list):
        problems.append("disagreements must be a list")

    regression = blob.get("regression")
    if isinstance(regression, dict):
        for key in ("resolved", "unchanged", "worsened", "new"):
            if not isinstance(regression.get(key), list):
                problems.append(f"regression.{key} must be a list")
    elif regression is not None:
        problems.append("regression must be an object")

    if blocker_ids and readiness in {"ready", "ready with minor revisions"}:
        problems.append(
            "publication_readiness cannot be ready while blocker findings exist"
        )

    corrections = blob.get("corrections")
    if corrections is not None:
        problems.extend(
            _validate_corrections(corrections, all_finding_ids)
        )

    return problems


def _validate_recommendation(
    index: int,
    recommendation: object,
    seen_rec_ids: set[str],
    all_finding_ids: set[str],
) -> list[str]:
    where = f"ranked_recommendations[{index}]"
    if not isinstance(recommendation, dict):
        return [f"{where} is not an object"]

    problems: list[str] = []
    for key in (
        "rec_id", "title", "need", "chosen_intervention", "rationale",
        "target_surface", "severity", "source_findings",
    ):
        if key not in recommendation:
            problems.append(f"{where}: missing key {key}")

    rec_id = recommendation.get("rec_id")
    if _nonempty_string(rec_id):
        if rec_id in seen_rec_ids:
            problems.append(f"{where}: duplicate rec_id {rec_id!r}")
        seen_rec_ids.add(rec_id)
    elif "rec_id" in recommendation:
        problems.append(f"{where}: rec_id must be a non-empty string")

    intervention = recommendation.get("chosen_intervention")
    if intervention is not None and intervention not in INTERVENTIONS:
        problems.append(
            f"{where}: chosen_intervention {intervention!r} not in "
            f"{sorted(INTERVENTIONS)}"
        )
    surface = recommendation.get("target_surface")
    if surface is not None and surface not in TARGET_SURFACES:
        problems.append(
            f"{where}: target_surface {surface!r} not in "
            f"{sorted(TARGET_SURFACES)}"
        )
    severity = recommendation.get("severity")
    if severity is not None and severity not in SEVERITIES:
        problems.append(f"{where}: severity {severity!r} not in {sorted(SEVERITIES)}")

    references = recommendation.get("source_findings")
    if not isinstance(references, list) or not references:
        problems.append(f"{where}: source_findings must be a non-empty list")
    else:
        for finding_id in references:
            if finding_id not in all_finding_ids:
                problems.append(
                    f"{where}: source finding {finding_id!r} has no matching finding_id"
                )
    return problems


def _validate_corrections(
    corrections: object, all_finding_ids: set[str]
) -> list[str]:
    if not isinstance(corrections, dict):
        return ["corrections must be an object"]

    problems: list[str] = []
    for key in (
        "status", "post_correction_readiness_estimate", "estimate_note",
        "applied", "remaining_high_priority", "verification",
    ):
        if key not in corrections:
            problems.append(f"corrections: missing key {key}")

    estimate = corrections.get("post_correction_readiness_estimate")
    if estimate is not None and estimate not in READINESS:
        problems.append(
            f"corrections.post_correction_readiness_estimate {estimate!r} "
            f"not in {sorted(READINESS)}"
        )

    applied = corrections.get("applied")
    if not isinstance(applied, list):
        problems.append("corrections.applied must be a list")
    else:
        for index, item in enumerate(applied):
            where = f"corrections.applied[{index}]"
            if not isinstance(item, dict):
                problems.append(f"{where} is not an object")
                continue
            if not _nonempty_string(item.get("change")):
                problems.append(f"{where}.change must be a non-empty string")
            for key in ("resolves", "partially_addresses"):
                references = item.get(key, [])
                if not isinstance(references, list):
                    problems.append(f"{where}.{key} must be a list")
                    continue
                for finding_id in references:
                    if finding_id not in all_finding_ids:
                        problems.append(
                            f"{where}.{key} references unknown finding "
                            f"{finding_id!r}"
                        )

    for key in ("remaining_high_priority", "verification"):
        value = corrections.get(key)
        if value is not None and not isinstance(value, list):
            problems.append(f"corrections.{key} must be a list")
    return problems


def _nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _sample_synthesized_report() -> dict:
    """Return a complete fixture used by selftest and regression tests."""
    personas = []
    for index, persona in enumerate(sorted(PERSONAS), start=1):
        finding_id = f"fixture-{index}"
        personas.append(
            {
                "persona": persona,
                "chapter_id": "demo",
                "summary": "ok",
                "overall_score": 7.0,
                "publication_blockers": [],
                "findings": [
                    {
                        "finding_id": finding_id,
                        "location": {"section_id": f"section-{index}"},
                        "severity": "medium",
                        "category": "conceptual-support",
                        "observation": "x",
                        "learner_impact": "y",
                        "recommended_outcome": "z",
                    }
                ],
            }
        )
    return {
        "chapter_id": "demo",
        "chapter_version": "1",
        "run_at": "2026-07-24T12:00:00Z",
        "personas": personas,
        "publication_readiness": "major revision",
        "executive_summary": "Demo report.",
        "consensus_strengths": ["Clear sequence."],
        "ranked_recommendations": [
            {
                "rec_id": "rec-001",
                "title": "Improve support",
                "need": "Learners need support.",
                "chosen_intervention": "prose-edit",
                "rationale": "A local edit is sufficient.",
                "target_surface": "prose",
                "severity": "medium",
                "source_findings": ["fixture-1"],
            }
        ],
        "accessibility_blockers": [],
        "visual_opportunities": [],
        "sufficient_as_is": [],
        "disagreements": [],
        "regression": {
            "resolved": [],
            "unchanged": [],
            "worsened": [],
            "new": ["fixture-1"],
        },
        "corrections": {
            "status": "applied-and-verified-without-second-persona-run",
            "post_correction_readiness_estimate": "major revision",
            "estimate_note": "Not a new persona verdict.",
            "applied": [
                {
                    "change": "Clarified the prose.",
                    "resolves": ["fixture-1"],
                    "partially_addresses": [],
                }
            ],
            "remaining_high_priority": [],
            "verification": ["selftest"],
        },
    }


def _selftest() -> int:
    good = {
        "persona": "Accessibility Persona",
        "chapter_id": "demo",
        "summary": "ok",
        "overall_score": 7.0,
        "publication_blockers": ["a-1"],
        "findings": [
            {
                "finding_id": "a-1",
                "location": {"asset_id": "mol-12"},
                "severity": "blocker",
                "category": "media-equivalence",
                "observation": "x",
                "learner_impact": "y",
                "recommended_outcome": "need z",
                "confidence": 0.9,
            }
        ],
    }
    assert validate(good) == [], validate(good)

    bad = {
        "persona": "Nobody",
        "chapter_id": "demo",
        "summary": "ok",
        "overall_score": 99,
        "publication_blockers": ["missing"],
        "findings": [
            {"finding_id": "f1", "location": {}, "severity": "catastrophic",
             "category": "made-up", "observation": "x", "learner_impact": "y",
             "recommended_outcome": "z"}
        ],
    }
    problems = validate(bad)
    for needle in ("unknown persona", "overall_score", "no resolvable anchor",
                   "severity", "category", "has no matching finding_id"):
        assert any(needle in p for p in problems), (needle, problems)

    report = _sample_synthesized_report()
    assert validate_synthesized_report(report) == [], validate_synthesized_report(report)
    report["ranked_recommendations"][0]["source_findings"] = ["missing-finding"]
    report_problems = validate_synthesized_report(report)
    assert any("missing-finding" in problem for problem in report_problems)

    print("selftest OK")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) not in (2, 3):
        print(__doc__, file=sys.stderr)
        return 2
    if argv[1] == "--selftest":
        if len(argv) != 2:
            print(__doc__, file=sys.stderr)
            return 2
        return _selftest()
    synthesized = argv[1] == "--synthesized"
    if synthesized and len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    if not synthesized and len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    path = argv[2] if synthesized else argv[1]
    raw = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
    try:
        blob = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"invalid JSON: {exc}", file=sys.stderr)
        return 1
    problems = validate_synthesized_report(blob) if synthesized else validate(blob)
    if problems:
        print("INVALID:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1
    print("valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
