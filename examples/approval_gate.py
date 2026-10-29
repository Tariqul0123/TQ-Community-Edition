"""Illustrative human-approval gate; no external actions."""
def authorize(action: str, *, approved_by_human: bool, high_impact: bool) -> bool:
    if high_impact and not approved_by_human:
        return False
    if action.strip().lower() in {"execute_trade", "delete_production", "publish_release"} and not approved_by_human:
        return False
    return True

if __name__ == "__main__":
    assert not authorize("execute_trade", approved_by_human=False, high_impact=True)
    assert authorize("read_report", approved_by_human=False, high_impact=False)
    print("approval gate example: OK")
