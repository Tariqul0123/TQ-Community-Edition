# Security Model

- The main TQ server is authoritative.
- Community code is separate from production state.
- Local AI is disposable inference compute, not an authoritative datastore.
- Keep credentials in a secret store or restricted files.
- Prefer loopback/private/encrypted transport.
- Do not expose inference endpoints publicly.
- Require human approval for irreversible/high-impact actions.
- Keep broker execution and automatic strategy mutation disabled unless explicitly approved.
