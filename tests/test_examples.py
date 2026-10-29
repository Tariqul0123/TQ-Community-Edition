import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "examples"))
from provider_router import Provider, choose_provider
from approval_gate import authorize
from learning_proposal import LearningProposal, approve

class ExampleTests(unittest.TestCase):
    def test_router_selects_eligible_provider(self):
        p = Provider("local", ("Background",), max_risk=0)
        self.assertEqual(choose_provider("Background", 0, (p,)).name, "local")

    def test_router_rejects_ineligible_risk(self):
        p = Provider("local", ("Background",), max_risk=0)
        with self.assertRaises(LookupError):
            choose_provider("Background", 1, (p,))

    def test_router_rejects_wrong_department(self):
        p = Provider("local", ("Background",), max_risk=1)
        with self.assertRaises(LookupError):
            choose_provider("Finance", 0, (p,))

    def test_high_impact_requires_approval(self):
        self.assertFalse(authorize("execute_trade", approved_by_human=False, high_impact=True))

    def test_low_impact_read_allowed(self):
        self.assertTrue(authorize("read_report", approved_by_human=False, high_impact=False))

    def test_learning_proposal_is_pending(self):
        p = LearningProposal("demo-1", "synthetic evidence", "test change")
        self.assertEqual(p.status, "pending_review")

    def test_learning_approval_requires_reviewer(self):
        p = LearningProposal("demo-1", "synthetic evidence", "test change")
        with self.assertRaises(ValueError):
            approve(p, "")

    def test_learning_approval_does_not_claim_implementation(self):
        p = LearningProposal("demo-1", "synthetic evidence", "test change")
        self.assertIn("separate_implementation_review", approve(p, "reviewer").status)

if __name__ == "__main__":
    unittest.main()
