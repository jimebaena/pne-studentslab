from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8081
FOLDER = "sequences/"
gene_name = "FRAT1"

c = Client(IP, PORT)
print(c)

s = Seq()
s.read_fasta(f"{FOLDER}{gene_name}.txt")

full_sequence = str(s)
print(f"Gene {gene_name}: {full_sequence}")

for i in range(5):
    start = i * 10
    end = start + 10
    fragment = full_sequence[start:end]

    print(f"Fragment {i + 1}: {fragment}")

    c.talk(fragment)

print("\nProcess finished with exit code 0")