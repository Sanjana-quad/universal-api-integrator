from pathlib import Path

root = Path(".")
input_dir = root / "input"
output_dir = root / "output"

# ensure folders exist
input_dir.mkdir(exist_ok=True)
output_dir.mkdir(exist_ok=True)

print("Folders created!")
