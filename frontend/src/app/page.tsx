import RepoForm from "@/components/RepoForm"

export default function Home() {
  return (
    <div>
      <p className="mb-4 text-gray-300">
        Paste a GitHub repository URL to analyze code quality, structure, and receive an AI roadmap.
      </p>
      <RepoForm />
    </div>
  )
}
