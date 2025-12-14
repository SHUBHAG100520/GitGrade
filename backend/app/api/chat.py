from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.services.chatbot_engine import chat_with_repo

router = APIRouter()

@router.post("/")
def chat_repo(request: ChatRequest):
    return chat_with_repo(request.repo_url, request.message)
