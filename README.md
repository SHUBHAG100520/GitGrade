🚀 GitGrade AI
AI-Powered GitHub Repository Evaluation Platform
GitGrade AI analyzes GitHub repositories using static analysis + AI reasoning (Gemini) to generate a quality score, summary, and improvement roadmap.

✨ Features

🔍 Static code & structure analysis

🧠 AI semantic reasoning using Gemini

📊 Score out of 100

🛣️ Actionable improvement roadmap

⚡ FastAPI backend + modern frontend

🧠 How It Works
flowchart LR
    A[User enters Repo URL] --> B[FastAPI Backend]
    B --> C[GitHub API]
    B --> D[Repo Cloner]
    D --> E[Static Analysis]
    E --> F[Gemini AI Analysis]
    F --> G[Scoring Engine]
    G --> H[JSON Response]

🏗️ System Architecture
graph TD
    UI[Frontend UI]
    API[FastAPI Backend]
    GH[GitHub API]
    AI[Gemini AI]
    FS[Repo Analyzer]

    UI --> API
    API --> GH
    API --> FS
    FS --> AI
    AI --> API

📊 Evaluation Metrics
Metric	Description
⭐ Stars	Repository popularity
🍴 Forks	Community usage
🧮 Complexity	Cyclomatic complexity
🗂 Structure	Folder & file organization
🧾 Commits	Commit discipline
🧠 AI Score	Semantic quality
📈 Score Composition (Example)
pie
    title GitGrade Score Breakdown
    "AI Semantic Quality" : 30
    "Code Structure" : 25
    "Complexity" : 20
    "Commit Discipline" : 15
    "Documentation" : 10

📉 Sample Quality Radar
radar
    title Repository Quality Radar
    metrics
        Structure: 80
        Complexity: 70
        Documentation: 65
        Commits: 75
        AI Quality: 85

🖥️ Frontend Preview

📌 Add screenshots in assets/ folder

![Dashboard](assets/dashboard.png)
![Score View](assets/score.png)
![Roadmap](assets/roadmap.png)

🧪 Example API Response
{
  "repository": "GitGrade-RealWorld",
  "score": 82,
  "summary": "Well-structured repository with clean code practices. AI suggests improving documentation and adding tests.",
  "roadmap": [
    "Add unit tests",
    "Improve README documentation",
    "Refactor long functions"
  ],
  "complexity": 12,
  "commits": {
    "rating": "Good",
    "suggestion": "Increase commit frequency"
  }
}

⚙️ Tech Stack
🧠 Backend

Python

FastAPI

GitPython

Requests

Gemini AI

🎨 Frontend

React / Next.js

Tailwind CSS

Chart.js / Recharts

🛠️ Installation & Setup
1️⃣ Clone Repo
git clone https://github.com/<your-username>/GitGrade-AI.git
cd GitGrade-AI

2️⃣ Backend Setup
cd backend
pip install -r requirements.txt


Create .env:

GEMINI_API_KEY=your_api_key_here


Run server:

python -m uvicorn app.main:app --reload

3️⃣ Frontend Setup
cd frontend
npm install
npm run dev

🔒 Environment Variables
Variable	Purpose
GEMINI_API_KEY	Gemini AI API key
GITHUB_API_BASE	GitHub REST API

👉 .env is NOT pushed to GitHub

📁 Project Structure
GitGrade-AI/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── services/
│   │   ├── core/
│   │   └── main.py
│   └── requirements.txt
├── frontend/
├── assets/
│   ├── banner.png
│   ├── dashboard.png
│   └── roadmap.png
├── .gitignore
└── README.md

🚨 Limitations

GitHub API rate limits

Very large repos may fail shallow clone

AI output depends on prompt quality

🌱 Future Improvements

🔐 GitHub OAuth login

🧪 Test coverage analysis

📊 Historical repo comparison

🌍 Multi-language support

🤖 Fine-tuned AI model

🏆 Hackathon Value

✔ Real-world problem
✔ AI + System Design
✔ Scalable backend
✔ Production-ready

👨‍💻 Author

Shubham Agarwal
B.Tech CSE (AI/ML) – VIT Bhopal
Cybersecurity | AI | Full Stack