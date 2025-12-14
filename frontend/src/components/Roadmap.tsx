export default function Roadmap({ items }) {
  return (
    <div className="bg-slate-800 p-4 rounded">
      <h3 className="font-semibold mb-2">Improvement Roadmap</h3>
      <ul className="list-disc ml-6">
        {items.map((item, i) => (
          <li key={i}>{item}</li>
        ))}
      </ul>
    </div>
  )
}
