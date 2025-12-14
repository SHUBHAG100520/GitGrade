# 🚀 GitGrade AI  
### AI-Powered GitHub Repository Evaluation Platform

GitGrade AI analyzes GitHub repositories using **static analysis + AI reasoning (Gemini)** to generate a **quality score, summary, and improvement roadmap**.

---

## ✨ Features

- 🔍 Static code & structure analysis  
- 🧠 AI semantic reasoning using **Gemini**  
- 📊 Repository score out of **100**  
- 🛣️ Actionable improvement roadmap  
- ⚡ FastAPI backend + modern frontend  

---

📊 Evaluation Metrics
Metric	Description
⭐ Stars	Repository popularity
🍴 Forks	Community adoption
🧮 Complexity	Cyclomatic complexity
🗂 Structure	Folder & file organization
🧾 Commits	Commit discipline
🧠 AI Score	Semantic quality

📈 Score Breakdown (Example)
mermaid
Copy code
pie
    title GitGrade Score Composition
    "AI Semantic Quality" : 30
    "Code Structure" : 25
    "Complexity" : 20
    "Commit Discipline" : 15
    "Documentation" : 10
🖥️ Frontend Preview
Add real screenshots inside the assets/ folder

md
Copy code
![Dashboard](assets/dashboard.png)
![Score View](assets/score.png)
![Roadmap](assets/roadmap.png)
🧪 Example API Response
json
Copy code
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
Backend
Python

FastAPI

GitPython

Requests

Gemini AI

Frontend
React / Next.js

Tailwind CSS

Chart.js / Recharts

🛠️ Installation & Setup
1️⃣ Clone Repository
bash
Copy code
git clone https://github.com/<your-username>/GitGrade-AI.git
cd GitGrade-AI
2️⃣ Backend Setup
bash
Copy code
cd backend
pip install -r requirements.txt
Create .env (do NOT commit):

env
Copy code
GEMINI_API_KEY=your_api_key_here
Run backend:

bash
Copy code
python -m uvicorn app.main:app --reload
3️⃣ Frontend Setup
bash
Copy code
cd frontend
npm install
npm run dev
🔒 Environment Variables
Variable	Purpose
GEMINI_API_KEY	Gemini AI API key
GITHUB_API_BASE	GitHub REST API

.env is intentionally ignored via .gitignore

📁 Project Structure
bash
Copy code
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
├── .gitignore
└── README.md
🚨 Limitations
GitHub API rate limits

Large repositories may fail shallow cloning

AI output depends on prompt quality

🌱 Future Improvements
GitHub OAuth login

Test coverage analysis

Historical repo comparison

Multi-language support

Fine-tuned AI model

🏆 Hackathon Value
✔ Real-world problem
✔ AI + System Design
✔ Scalable backend
✔ Production-ready

👨‍💻 Author
Aman  Agarwal
B.Tech CSE (AI/ML) – VIT Bhopal
Cybersecurity | AI | Full Stack

⭐ If you like this project, please give it a star!

yaml
Copy code

---

## ✅ Final checklist for graphs to appear

- [ ] README uses ```mermaid blocks
- [ ] No radar charts
- [ ] Images exist in `assets/`
- [ ] Repo is public
- [ ] Markdown copied exactly

---

If you want, next I can:
- Convert radar → image
- Create **frontend charts**
- Generate **hackathon PPT**
- Optimize **Gemini prompt**

Just tell me 🚀






