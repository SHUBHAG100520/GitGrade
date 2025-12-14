from app.core.prompts import REPO_EVALUATION_PROMPT

def ai_evaluate(metadata, complexity, commit_info):
    # Replace this with OpenAI / Gemini call
    return {
        "score": min(100, 50 + int(complexity * 5)),
        "summary": "Project has good structure but needs better testing and documentation.",
        "roadmap": [
            "Add unit tests",
            "Reduce cyclomatic complexity",
            "Improve README documentation",
            "Add CI/CD pipeline"
        ]
    }
