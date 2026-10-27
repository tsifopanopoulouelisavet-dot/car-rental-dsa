from pathlib import Path
import subprocess
import sys

# Run every test file using the same Python interpreter.
folder = Path(__file__).resolve().parent
test_files = sorted(folder.glob("test_*.py"))

for test_file in test_files:
    print(f"\nRunning {test_file.name}", flush=True)
    subprocess.run(
        [sys.executable, str(test_file)],
        cwd=folder,
        check=True,
    )

print(f"\nAll {len(test_files)} test files passed.")