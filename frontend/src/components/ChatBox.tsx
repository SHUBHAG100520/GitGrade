"use client"

import { useState } from "react"
import { chatWithRepo } from "@/lib/api"

export default function ChatBox({ repoUrl }) {
  const [messages, setMessages] = useState<any[]>([])
  const [input, setInput] = useState("")

  const send = async () => {
    if (!input) return
    const res = await chatWithRepo(repoUrl, input)

    setMessages([
      ...messages,
      { role: "user", text: input },
      { role: "ai", text: res.answer },
    ])

    setInput("")
  }

  return (
    <div className="bg-slate-800 p-4 rounded">
      <div className="h-64 overflow-y-auto mb-2">
        {messages.map((m, i) => (
          <p key={i} className={m.role === "ai" ? "text-green-400" : ""}>
            <b>{m.role}:</b> {m.text}
          </p>
        ))}
      </div>

      <input
        value={input}
        onChange={e => setInput(e.target.value)}
        className="w-full p-2 text-black rounded"
        placeholder="Ask how to improve your repo..."
      />
      <button onClick={send} className="mt-2 bg-blue-600 px-4 py-1 rounded">
        Send
      </button>
    </div>
  )
}
