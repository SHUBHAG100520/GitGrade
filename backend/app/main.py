from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.analyze import router as analyze_router
from app.api.chat import router as chat_router

app = FastAPI(
    title="GitGrade AI",
    description="AI-powered GitHub Repository Evaluator",
    version="1.0"
)

# ✅ CORS CONFIG (THIS FIXES FAILED TO FETCH)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze_router, prefix="/analyze", tags=["Analysis"])
app.include_router(chat_router, prefix="/chat", tags=["Chatbot"])

@app.get("/")
def root():
    return {"status": "GitGrade AI backend running"}
