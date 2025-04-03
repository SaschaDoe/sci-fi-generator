import sys
from pathlib import Path

# Dynamically add the root/src directory to sys.path
project_root = Path(__file__).resolve().parent.parent
src_path = project_root / "src"

if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

print("🛠 PYTHONPATH:", sys.path)