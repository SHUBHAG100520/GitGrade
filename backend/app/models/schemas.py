from pydantic import BaseModel
from typing import List

class RepoRequest(BaseModel):
    repo_url: str

class ChatRequest(BaseModel):
    repo_url: str
    message: str

class AnalysisResponse(BaseModel):
    score: int
    summary: str
    roadmap: List[str]
