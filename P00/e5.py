from Seq0 import seq_read_fasta, seq_count

FOLDER = "sequences/"
GENES = ["U5", "ADA", "FRAT1", "FXN"]


if __name__ == "__main__":
    print("-----| Exercise 5 |------")

    for gene in GENES:
        filename = f"{FOLDER}{gene}.txt"
        sequence = seq_read_fasta(filename)

        diccionario_bases = seq_count(sequence)

        print(f"Gene {gene}: {diccionario_bases}")

