#!/usr/bin/env python3
"""Validate roadmap state. Read-only; no product access or network calls."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TERMINAL = {"VERIFIED"}
ACTIVE = {"READY", "IN_PROGRESS", "BLOCKED"}
DEPLOYMENT = {"NOT_APPLIED", "PILOT", "APPROVED_LIVE", "DEFERRED"}


def validate(data, root=ROOT):
    if not isinstance(data, dict) or data.get("schema_version") != 2:
        return ["unsupported schema_version"]
    try:
        plan = json.loads((ROOT / "state/stage-plan.json").read_text(encoding="utf-8"))["stages"]
    except (OSError, ValueError, KeyError, TypeError):
        return ["stage plan missing or invalid"]
    stages = data.get("stages")
    if not isinstance(stages, list) or len(stages) != len(plan) or len(plan) != 22:
        return ["expected 22 stages"]
    errors = []
    unfinished = False
    for i, s in enumerate(stages):
        expected = plan[i]
        sid = expected["id"]
        if not isinstance(s, dict):
            errors.append(f"{sid}: invalid record")
            continue
        if any(s.get(key) != expected[key] for key in ("id", "horizon", "title", "guide")) or s.get("conditional") is not False:
            errors.append(f"{sid}: plan identity/order or mandatory-learning policy mismatch")
        status = s.get("status")
        if status not in TERMINAL | ACTIVE | {"PENDING"}:
            errors.append(f"{sid}: invalid status")
        guide = s.get("guide")
        if not isinstance(guide, str) or not guide.startswith(f"docs/stages/{sid}-") or not safe_file(root, guide, "docs/stages"):
            errors.append(f"{sid}: guide missing or invalid")
        if unfinished and status != "PENDING":
            errors.append(f"{sid}: earlier stage unfinished")
        if not unfinished and status == "PENDING":
            errors.append(f"{sid}: earliest unfinished stage must be READY, IN_PROGRESS or BLOCKED")
        if status in ACTIVE and not nonempty(s.get("next_action")):
            errors.append(f"{sid}: next_action required")
        if status == "BLOCKED" and not nonempty(s.get("blocker")):
            errors.append(f"{sid}: blocker required")
        if status in TERMINAL | {"IN_PROGRESS", "BLOCKED"}:
            if not safe_file(root, s.get("report"), "records", prefix=sid + "-"):
                errors.append(f"{sid}: existing stage report required")
        if status == "DEFERRED":
            errors.append(f"{sid}: deferral requires completed learning; defer deployment only")
        deployment = s.get("deployment")
        if deployment not in DEPLOYMENT:
            errors.append(f"{sid}: invalid deployment status")
        if deployment in {"PILOT", "APPROVED_LIVE", "DEFERRED"} and (status != "VERIFIED" or not nonempty(s.get("approval_ref"))):
            errors.append(f"{sid}: deployment requires verification and approval reference")
        if deployment == "DEFERRED" and not nonempty(s.get("defer_reason")):
            errors.append(f"{sid}: deployment deferral reason required")
        if status not in TERMINAL:
            unfinished = True
    return errors


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def safe_file(root, value, folder, prefix=""):
    if not nonempty(value):
        return False
    try:
        candidate = (root / value).resolve()
        base = (root / folder).resolve()
        return candidate.is_relative_to(base) and candidate.is_file() and candidate.name.startswith(prefix) and candidate.suffix == ".md"
    except (OSError, ValueError):
        return False


def main():
    try:
        data = json.loads((ROOT / "state/progress.json").read_text(encoding="utf-8"))
        errors = validate(data)
    except (OSError, ValueError, TypeError) as e:
        print(f"INVALID: {e}", file=sys.stderr)
        return 1
    if errors:
        print("INVALID:\n- " + "\n- ".join(errors), file=sys.stderr)
        return 1
    next_stage = next((s for s in data["stages"] if s["status"] not in TERMINAL), None)
    print("PASS: roadmap state structure and sequence")
    if next_stage:
        print(f"CURRENT: {next_stage['id']} / {next_stage['horizon']} / {next_stage['title']} / {next_stage['status']}")
        print(f"GUIDE: {next_stage['guide']}")
        print(f"NEXT: {next_stage['next_action']}")
        if next_stage["status"] == "BLOCKED":
            print(f"BLOCKER: {next_stage['blocker']}")
    else:
        print("All 22 initial stages verified; continue operational measurement and review.")
    print("NOTE: structural validation only; not product verification or deployment approval.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
