from fastapi import APIRouter
from pydantic import BaseModel
from app.services.pipeline import run_full_analysis

router = APIRouter()

class RepoRequest(BaseModel):
    repo_url: str

@router.post("/")
def analyze_repo(request: RepoRequest):
    return run_full_analysis(request.repo_url)
