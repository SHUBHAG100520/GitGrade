import os
import json

from app.services.github_fetcher import fetch_repo_metadata
from app.services.repo_cloner import clone_repo
from app.services.complexity import calculate_complexity
from app.services.commit_eval import evaluate_commits
from app.services.structure_eval import evaluate_structure
from app.services.ai_analyzer import ai_analyze_repo


def run_full_analysis(repo_url: str):
    """
    Runs full repository analysis using:
    - GitHub metadata
    - Shallow repo clone
    - Radon complexity
    - Commit heuristics
    - Structure rules
    - Gemini AI semantic analysis
    """

    # 1️⃣ GitHub metadata (SAFE, API-based)
    metadata = fetch_repo_metadata(repo_url)

    # 2️⃣ Repo clone (SAFE, shallow, may fail gracefully)
    repo_path = clone_repo(repo_url)

    # 3️⃣ Code complexity (ONLY if repo cloned correctly)
    if repo_path and os.path.exists(repo_path):
        try:
            complexity = calculate_complexity(repo_path)
        except Exception as e:
            print(f"[WARN] Complexity analysis failed: {e}")
            complexity = {
                "average": 0,
                "max": 0,
                "files": 0
            }
    else:
        complexity = {
            "average": 0,
            "max": 0,
            "files": 0
        }

    # 4️⃣ Commit & structure heuristics
    commit_info = evaluate_commits(metadata.get("commit_count", 0))
    structure_suggestions = evaluate_structure(metadata)

    # 5️⃣ AI semantic analysis (Gemini)
    try:
        ai_raw = ai_analyze_repo(metadata, complexity, commit_info)

        ai_result = json.loads(ai_raw)

    except Exception as e:
        print(f"[WARN] AI analysis failed: {e}")
        ai_result = {
            "score": 50,
            "summary": "AI analysis failed. Static analysis applied.",
            "roadmap": []
        }

    # 6️⃣ Merge AI + rule-based suggestions
    final_roadmap = list(set(
        ai_result.get("roadmap", []) + structure_suggestions
    ))

    # 7️⃣ Final response (STABLE, NEVER CRASHES)
    return {
        "repository": metadata.get("name", "unknown"),
        "score": ai_result.get("score", 50),
        "summary": ai_result.get("summary", ""),
        "roadmap": final_roadmap,
        "complexity": complexity,
        "commits": commit_info
    }
