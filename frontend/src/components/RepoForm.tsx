"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"

export default function RepoForm() {
  const [url, setUrl] = useState("")
  const router = useRouter()

  const submit = () => {
    if (!url) return
    router.push(`/analyze?repo=${encodeURIComponent(url)}`)
  }

  return (
    <div className="flex gap-2">
      <input
        value={url}
        onChange={e => setUrl(e.target.value)}
        placeholder="https://github.com/user/repo"
        className="w-full p-2 rounded text-black"
      />
      <button
        onClick={submit}
        className="bg-blue-600 px-4 rounded"
      >
        Analyze
      </button>
    </div>
  )
}
