import json
import tempfile
import unittest
from pathlib import Path
from scripts.check_progress import ROOT, validate


class ProgressTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "state/progress.json").read_text(encoding="utf-8"))
        # Use a synthetic initial state for transition tests so they remain valid
        # after real project progress has been recorded.
        for i, stage in enumerate(self.data["stages"]):
            stage.update(status="READY" if i == 0 else "PENDING",
                         deployment="NOT_APPLIED", report=None, blocker=None,
                         defer_reason=None, approval_ref=None,
                         next_action="initial synthetic action" if i == 0 else None)

    def test_current_state(self):
        data = json.loads((ROOT / "state/progress.json").read_text(encoding="utf-8"))
        self.assertEqual(validate(data), [])

    def test_initial_state(self):
        self.assertEqual(validate(self.data), [])

    def test_parallel_stage_rejected(self):
        self.data["stages"][1].update(status="READY", next_action="premature")
        self.assertTrue(any("earlier stage unfinished" in e for e in validate(self.data)))

    def test_missing_report_rejected(self):
        self.data["stages"][0]["status"] = "VERIFIED"
        self.data["stages"][1].update(status="READY", next_action="next")
        self.assertTrue(any("report required" in e for e in validate(self.data)))

    def test_unapproved_deferral_rejected(self):
        self.data["stages"][0].update(status="DEFERRED", defer_reason="not allowed")
        self.assertTrue(any("deferral requires" in e for e in validate(self.data)))

    def test_missing_blocker_rejected(self):
        self.data["stages"][0]["status"] = "BLOCKED"
        self.assertTrue(any("blocker required" in e for e in validate(self.data)))

    def test_deployment_without_approval_rejected(self):
        self.data["stages"][0]["deployment"] = "APPROVED_LIVE"
        self.assertTrue(any("deployment requires" in e for e in validate(self.data)))

    def test_path_escape_rejected(self):
        self.data["stages"][0]["guide"] = "docs/stages/AX-00-../../README.md"
        self.assertTrue(any("guide missing" in e for e in validate(self.data)))

    def test_valid_transition(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "docs/stages").mkdir(parents=True)
            (root / "records").mkdir()
            for stage in self.data["stages"]:
                (root / stage["guide"]).write_text("test fixture", encoding="utf-8")
            (root / "records/AX-00-20261126.md").write_text("test fixture", encoding="utf-8")
            self.data["stages"][0].update(status="VERIFIED", report="records/AX-00-20261126.md", next_action=None)
            self.data["stages"][1].update(status="READY", next_action="next")
            self.assertEqual(validate(self.data, root), [])


if __name__ == "__main__":
    unittest.main()
