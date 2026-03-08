from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8081
FOLDER = "sequences/"
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]


c = Client(IP, PORT)

for gene_name in genes:
    s = Seq()
    s.read_fasta(f"{FOLDER}{gene_name}.txt")

    msg_intro = f"Sending {gene_name} Gene to the server..."


    print(f"To Server: {msg_intro}")
    response1 = c.talk(msg_intro)
    print(f"From Server: {response1}\n")

    print(f"To Server: {str(s)}")
    response2 = c.talk(str(s))
    print(f"From Server: {response2}\n")

print("\nProcess finished successfully.")