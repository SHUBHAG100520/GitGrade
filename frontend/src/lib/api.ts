const BACKEND_URL = "http://localhost:8000";

export async function analyzeRepo(repoUrl: string) {
  try {
    const res = await fetch(`${BACKEND_URL}/analyze/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        repo_url: repoUrl,
      }),
    });

    if (!res.ok) {
      const text = await res.text();
      throw new Error(`Backend error: ${text}`);
    }

    return await res.json();
  } catch (error) {
    console.error("Analyze API failed:", error);
    throw error;
  }
}

export async function chatWithRepo(repoUrl: string, message: string) {
  try {
    const res = await fetch(`${BACKEND_URL}/chat/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        repo_url: repoUrl,
        message: message,
      }),
    });

    if (!res.ok) {
      const text = await res.text();
      throw new Error(`Backend error: ${text}`);
    }

    return await res.json();
  } catch (error) {
    console.error("Chat API failed:", error);
    throw error;
  }
}
