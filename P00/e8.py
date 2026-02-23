from Seq0 import seq_read_fasta, frequency

FOLDER = "sequences/"
U5 = "U5.txt"
ADA = "ADA.txt"
FRAT1 = "FRAT1.txt"
FXN = "FXN.txt"

if __name__ == "__main__":
    print("-----| Exercise 7 |------")
    FILES = [U5, ADA, FRAT1, FXN]
    for file in FILES:
        full_path = FOLDER + file
        seq = seq_read_fasta(full_path)
        result = frequency(seq)
        name = file.replace(".txt", "")
        print("Gene", name, ": Most frequent base:", result)