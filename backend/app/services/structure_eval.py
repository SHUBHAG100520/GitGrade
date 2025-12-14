def evaluate_structure(metadata: dict) -> list:
    suggestions = []

    if not metadata["has_readme"]:
        suggestions.append("Add a detailed README.md")

    if "tests" not in [f.lower() for f in metadata["folders"]]:
        suggestions.append("Add a tests/ directory with unit tests")

    return suggestions
