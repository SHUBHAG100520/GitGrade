from app.services.pipeline import run_full_analysis

def chat_with_repo(repo_url: str, message: str):
    analysis = run_full_analysis(repo_url)

    return {
        "question": message,
        "answer": f"To improve your score, focus on: {', '.join(analysis['roadmap'][:2])}"
    }
