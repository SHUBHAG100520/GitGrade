"use client"

import { useSearchParams } from "next/navigation"
import ChatBox from "@/components/ChatBox"

export default function ChatPage() {
  const params = useSearchParams()
  const repo = params.get("repo") || ""

  return <ChatBox repoUrl={repo} />
}
