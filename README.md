# TQ Community Edition (Reconstructed Release)

TQ is designed around a stable core that owns policy, workflows, memory, and business state. AI providers and Local AI are replaceable workers—not authoritative stores.

> **Release status: OWNER-APPROVED PUBLIC RELEASE UNDER A DOCUMENTED EXCEPTION.** This package was reconstructed from project notes because the original `TQ_COMMUNITY_EDITION_RELEASE_V7.zip` was unavailable. It is not byte-identical to the previous V7 archive. The repository owner explicitly waived the dedicated Gitleaks scan, independent human licensing/provenance review, and hosted GitHub Actions CI as pre-publication gates. Those checks are not represented as passed. Check the repository's actual Actions results after publication.

## Goals
- Demonstrate modular AI provider routing.
- Keep approval gates around high-impact actions.
- Represent learning as versioned proposals rather than silently mutating strategy.
- Keep demo/test data isolated from real business data.
- Keep authoritative TQ state on the private main server.

## Safety boundary
This repository is an example/reference package, not a production deployment recipe. Do not connect it to production credentials, databases, broker accounts, or private services. Never expose Local AI inference publicly. Use synthetic data only in demos. Human approval is required for irreversible or high-impact actions.

## Quick start
Requires Python 3.10+ and uses only the Python standard library.

```bash
python -m unittest discover -s tests -v
python tools/scan_public_release.py .
```

The examples are illustrative and do not connect to any external provider or execute trades.

## Community contributions
Read [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and [PUBLIC-SAFETY-CHECKLIST.md](PUBLIC-SAFETY-CHECKLIST.md) before contributing.

## Current limitations
- No hosted demo is included.
- No authentication, database, web server, or deployment automation is implemented.
- Examples do not establish production readiness.
- Dedicated secret scanning and independent legal/provenance review were waived by explicit owner decision for this publication; hosted CI must be checked separately and is not assumed to pass. See [OWNER-APPROVED-EXCEPTION.md](OWNER-APPROVED-EXCEPTION.md) and [RELEASE-STATUS.md](RELEASE-STATUS.md).
