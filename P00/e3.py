
from Seq0 import seq_read_fasta, seq_len

FOLDER = "sequences/"
GENES = ["U5", "ADA", "FRAT1", "FXN"]

if __name__ == "__main__":
    print("-----| Exercise 3 |------")

    for gene_name in GENES:
        filename = f"{gene_name}.txt"
        full_path = FOLDER + filename

        sequence = seq_read_fasta(full_path)
        length = seq_len(sequence)
        print(f"Gene {gene_name} -> Length: {length}")



