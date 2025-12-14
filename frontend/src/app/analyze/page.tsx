"use client"

import { useSearchParams } from "next/navigation"
import { useEffect, useState } from "react"
import { analyzeRepo } from "@/lib/api"
import ScoreCard from "@/components/ScoreCard"
import Roadmap from "@/components/Roadmap"

export default function AnalyzePage() {
  const params = useSearchParams()
  const repo = params.get("repo")
  const [data, setData] = useState<any>(null)

  useEffect(() => {
    if (repo) analyzeRepo(repo).then(setData)
  }, [repo])

  if (!data) return <p>Analyzing repository...</p>

  return (
    <div className="space-y-4">
      <ScoreCard score={data.score} summary={data.summary} />
      <Roadmap items={data.roadmap} />
      <a
        href={`/chat?repo=${encodeURIComponent(repo!)}`}
        className="text-blue-400 underline"
      >
        Chat with AI Mentor →
      </a>
    </div>
  )
}
