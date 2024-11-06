from pathlib import Path

path = Path(__file__).parent / "input.txt"
lines = path.read_text().split("\n\n")

nums = map(int, lines.pop(0).split(","))
print(nums)
