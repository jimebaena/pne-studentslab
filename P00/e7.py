from Seq0 import seq_read_fasta, seq_complement

FOLDER = "sequences/"
FILENAME = "U5.txt"


if __name__ == "__main__":
    print("-----| Exercise 7 |------")

    full_path = FOLDER + FILENAME
    sequence = seq_read_fasta(full_path)

    fragment = sequence[:20]

    complement_fragment = seq_complement(fragment)

    print(f"Gene {FILENAME.replace('.txt', '')}:")
    print(f"Frag: {fragment}")
    print(f"Comp: {complement_fragment}")

