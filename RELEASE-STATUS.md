# Release Status

**Status: OWNER-APPROVED PUBLICATION UNDER AN EXCEPTION — WAIVED GATES NOT PASSED**

This is a reconstructed community-edition release, not a byte-identical copy of the historical V7 archive. The repository owner explicitly authorized publication while accepting the residual risk of three incomplete pre-publication gates. This is a documented exception, not a claim that the waived checks passed.

## Owner-approved exceptions
- **Dedicated Gitleaks scan:** waived before publication; not run against the exact final published Git tree.
- **Independent human licensing/provenance review:** waived before publication; no independent review is claimed.
- **GitHub Actions CI:** waived as a pre-publication gate. The workflow is included; inspect the actual post-publication run result and do not assume it passed.

The owner's prior attestation states they have the right to publish all candidate files under Apache-2.0. This report records that attestation as owner-provided information, not as independent legal advice or verification.

## Local evidence
- Candidate source archive integrity and archive safety checks passed.
- Unit tests: 8/8 passed locally.
- Python compilation passed locally.
- Built-in heuristic scanner passed locally.
- Extended selected secret-pattern scans returned no findings for the patterns checked. These checks are not equivalent to Gitleaks and are not a security certification.

## Publication verification
The target repository's commit history and file tree are the source of truth for what was published. Check the actual GitHub Actions run after publication; this document does not claim hosted CI passed. The private production repository `Tariqul0123/tq-command-centre` is outside the release scope and must remain private and unchanged.

## Safety boundary
- This public repository contains only the community-edition reference package; it is not a production deployment recipe.
- Do not add production credentials, private data, broker connections, or deployment secrets.
- Human approval remains required for irreversible/high-impact actions.

See [OWNER-APPROVED-EXCEPTION.md](OWNER-APPROVED-EXCEPTION.md) and [RELEASE-AUDIT-REPORT.md](RELEASE-AUDIT-REPORT.md) for the recorded decision and limitations.
