import os
from radon.complexity import cc_visit

def calculate_complexity(repo_path: str) -> float:
    total_complexity = 0
    blocks = 0

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                try:
                    code = open(os.path.join(root, file), encoding="utf-8").read()
                    results = cc_visit(code)
                    for r in results:
                        total_complexity += r.complexity
                        blocks += 1
                except:
                    pass

    return round(total_complexity / blocks, 2) if blocks else 0
