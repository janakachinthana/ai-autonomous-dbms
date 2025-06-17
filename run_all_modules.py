import sys
import os
sys.path.insert(0, os.path.abspath("src"))
import subprocess
import sys

modules = [
    ("Intelligent Indexing Module", "src/intelligent_indexing/main.py"),
    ("Predictive Query Optimizer", "src/query_optimization/main.py"),
    ("Security & Compliance Layer", "src/security/main.py"),
    ("Self-Tuning Engine", "src/self_tuning/main.py"),
]

for name, path in modules:
    print(f"\n=== Running: {name} ===")
    result = subprocess.run([sys.executable, path], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"[Error Output]\n{result.stderr}")
