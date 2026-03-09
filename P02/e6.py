from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT1 = 8080
PORT2 = 8081
FOLDER = "sequences/"


c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

print(c1)
print(c2)


s = Seq()
s.read_fasta(f"{FOLDER}FRAT1.txt")
full_sequence = str(s)
print(f"Gene FRAT1: {full_sequence}")

for i in range(10):
    start = i * 10
    end = start + 10
    fragment = full_sequence[start:end]

    num_fragment = i + 1
    msg_to_send = f"Fragment {num_fragment}: {fragment}"
    print(msg_to_send)

    if num_fragment % 2 != 0:
        c1.talk(msg_to_send)
    else:
        c2.talk(msg_to_send)

print("\nProcess finished with exit code 0")