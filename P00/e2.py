
from Seq0 import seq_read_fasta

FOLDER = "sequences/"
FILENAME = "U5.txt"

if __name__ == "__main__":
    full_path = FOLDER + FILENAME

    dna_sequence = seq_read_fasta(full_path)
    print(f"DNA file: {FILENAME}")

    first_20 = dna_sequence[:20]
    print(f"The first 20 bases are: {first_20}")

