from pathlib import Path

FILENAME = "sequences/ADA.txt"

file_contents = Path(FILENAME).read_text()

n = file_contents.find("\n")
body = file_contents[n:]
bases = body.replace("\n", "")
print("The total number of bases in ADA is:", len(bases))
