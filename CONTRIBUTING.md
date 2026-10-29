# Contributing

1. Open an issue to discuss substantial changes before implementation.
2. Keep changes small, documented, and testable.
3. Do not include production endpoints, credentials, customer data, private memory, or internal-only policy.
4. Use synthetic fixtures for tests and demos.
5. Add or update tests for behavior changes.
6. Run:
   ```bash
   python -m unittest discover -s tests -v
   python tools/scan_public_release.py .
   ```
7. Submit a pull request with the purpose, test results, risk, and rollback notes.

Do not add automated trading execution, automatic strategy mutation, or irreversible actions without an explicit reviewed design and human approval gate.
