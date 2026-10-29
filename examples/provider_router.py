"""Illustrative provider routing; no network calls or secrets."""
from dataclasses import dataclass
from typing import Mapping

@dataclass(frozen=True)
class Provider:
    name: str
    departments: tuple[str, ...]
    enabled: bool = True
    max_risk: int = 1

def choose_provider(department: str, risk: int, providers: tuple[Provider, ...]) -> Provider:
    """Choose the first enabled provider allowed for the department/risk."""
    for provider in providers:
        if provider.enabled and department in provider.departments and risk <= provider.max_risk:
            return provider
    raise LookupError("No eligible provider; require fallback or human review")

if __name__ == "__main__":
    providers = (
        Provider("example-api-worker", ("General", "Research"), max_risk=1),
        Provider("local-ai-worker", ("Background",), max_risk=0),
    )
    print(choose_provider("Background", 0, providers).name)
