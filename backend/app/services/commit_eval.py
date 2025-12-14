def evaluate_commits(commit_count: int) -> str:
    if commit_count > 50:
        return "Excellent commit consistency"
    elif commit_count > 20:
        return "Moderate commit history"
    else:
        return "Poor or infrequent commits"
