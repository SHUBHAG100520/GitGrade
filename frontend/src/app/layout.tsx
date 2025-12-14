import "./globals.css"

export const metadata = {
  title: "GitGrade AI",
  description: "AI-powered GitHub Repository Evaluator",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="bg-slate-900 text-white">
        <div className="max-w-5xl mx-auto p-6">
          <h1 className="text-3xl font-bold mb-6">🚀 GitGrade AI</h1>
          {children}
        </div>
      </body>
    </html>
  )
}
