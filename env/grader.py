def grade_review(agent_review, expected):

    review = agent_review.lower()
    expected = expected.lower()

    # exact solution
    if expected in review:
        return 1.0

    # partial matches for specific issues
    if "indentation" in review or "indent" in review:
        return 1.0

    if "sql injection" in review or "sql" in review:
        return 1.0

    if "hardcoded password" in review or "hardcoded" in review:
        return 1.0

    # general bug/issue detection
    if "bug" in review or "issue" in review or "error" in review or "problem" in review:
        return 0.5

    return 0.0