import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def ai_analyze_repo(metadata, complexity, commit_info):
    prompt = f"""
You are a senior software engineer and code reviewer.

Analyze this GitHub repository and return a JSON response.

Repository Name: {metadata['name']}
Stars: {metadata['stars']}
Commits: {metadata['commit_count']}
Has README: {metadata['has_readme']}
Languages: {metadata.get('languages')}
Average Complexity: {complexity}
Commit Quality: {commit_info}

Tasks:
1. Give a score from 0 to 100
2. Write a short summary (2–3 lines)
3. Provide 5 improvement roadmap points

Return ONLY valid JSON like:
{{
  "score": number,
  "summary": string,
  "roadmap": []
}}
"""

    response = model.generate_content(prompt)

    return response.text
