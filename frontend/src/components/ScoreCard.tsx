export default function ScoreCard({ score, summary }) {
  return (
    <div className="bg-slate-800 p-4 rounded">
      <h2 className="text-xl font-bold">Score: {score}/100</h2>
      <p className="text-gray-300 mt-2">{summary}</p>
    </div>
  )
}
