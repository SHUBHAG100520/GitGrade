import git
import tempfile
import os

def clone_repo(repo_url: str) -> str:
    temp_dir = tempfile.mkdtemp()

    try:
        git.Repo.clone_from(
            repo_url,
            temp_dir,
            depth=1,              # ✅ shallow clone
            no_single_branch=True,
            multi_options=["--filter=blob:none"]  # ✅ avoid big files
        )
        return temp_dir

    except Exception as e:
        # ✅ DO NOT crash app
        print(f"[WARN] Repo clone failed: {e}")
        return temp_dir  # return empty dir safely
