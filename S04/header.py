from pathlib import Path

FILENAME = "sequences/RNU6_269P.txt"

file_contents = Path(FILENAME).read_text()
t = file_contents.find("\n")
print(file_contents[0:t])