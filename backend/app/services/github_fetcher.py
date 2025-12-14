import requests
from app.core.config import GITHUB_API_BASE

HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "GitGrade-AI"
}


def fetch_repo_metadata(repo_url: str):
    owner, repo = repo_url.rstrip("/").split("/")[-2:]

    repo_api = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    commits_api = f"{repo_api}/commits"
    contents_api = f"{repo_api}/contents"
    languages_api = f"{repo_api}/languages"

    try:
        repo_resp = requests.get(repo_api, headers=HEADERS, timeout=10)
        commits_resp = requests.get(commits_api, headers=HEADERS, timeout=10)
        contents_resp = requests.get(contents_api, headers=HEADERS, timeout=10)
        languages_resp = requests.get(languages_api, headers=HEADERS, timeout=10)

        repo_data = repo_resp.json()
        commits_data = commits_resp.json()
        contents_data = contents_resp.json()
        languages_data = languages_resp.json()

    except Exception as e:
        print(f"[WARN] GitHub API request failed: {e}")
        return _fallback_metadata(repo)

    # ✅ SAFETY CHECKS
    if not isinstance(contents_data, list):
        contents_data = []

    if not isinstance(commits_data, list):
        commits_data = []

    if not isinstance(languages_data, dict):
        languages_data = {}

    files = []
    folders = []

    for item in contents_data:
        if not isinstance(item, dict):
            continue
        if item.get("type") == "file":
            files.append(item.get("name"))
        elif item.get("type") == "dir":
            folders.append(item.get("name"))

    return {
        "name": repo,
        "stars": repo_data.get("stargazers_count", 0),
        "forks": repo_data.get("forks_count", 0),
        "open_issues": repo_data.get("open_issues_count", 0),
        "commit_count": len(commits_data),
        "files": files,
        "folders": folders,
        "languages": list(languages_data.keys()),   # ✅ FIXED
        "has_readme": any(
            f.lower().startswith("readme") for f in files
        ),
    }


def _fallback_metadata(repo_name: str):
    return {
        "name": repo_name,
        "stars": 0,
        "forks": 0,
        "open_issues": 0,
        "commit_count": 0,
        "files": [],
        "folders": [],
        "languages": [],
        "has_readme": False
    }
