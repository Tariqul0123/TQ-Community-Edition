"""Learning is proposed and versioned; this example never mutates a strategy."""
from dataclasses import dataclass

@dataclass(frozen=True)
class LearningProposal:
    proposal_id: str
    evidence_summary: str
    proposed_change: str
    status: str = "pending_review"

def approve(proposal: LearningProposal, reviewer: str) -> LearningProposal:
    if not reviewer.strip():
        raise ValueError("A named reviewer is required")
    return LearningProposal(
        proposal_id=proposal.proposal_id,
        evidence_summary=proposal.evidence_summary,
        proposed_change=proposal.proposed_change,
        status="approved_for_separate_implementation_review",
    )
