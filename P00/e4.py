from Seq0 import seq_read_fasta, seq_count_base

FOLDER = "sequences/"
GENES = ["U5", "ADA", "FRAT1", "FXN"]
BASES = ["A", "C", "T", "G"]

if __name__ == "__main__":
    print("-----| Exercise 4 |------")

    for gene in GENES:
        filename = f"{FOLDER}{gene}.txt"
        sequence = seq_read_fasta(filename)
        result = f"Gene {gene}:\n"
        for base in BASES:
            count = seq_count_base(sequence, base)
            result += f"  {base}: {count}\n"
        print(result)

