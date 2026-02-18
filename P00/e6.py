from Seq0 import seq_read_fasta, seq_reverse

FOLDER = "sequences/"
FILENAME = "U5.txt"


if __name__ == "__main__":
    print("------| Exercise 6 |------")

    full_path = FOLDER + FILENAME
    sequence = seq_read_fasta(full_path)

    fragment = sequence[:20]

    reversed_fragment = seq_reverse(sequence, 20)

    print(f"Gene {FILENAME.replace('.txt', '')}")
    print(f"Fragment: {fragment}")
    print(f"Reverse:  {reversed_fragment}")



