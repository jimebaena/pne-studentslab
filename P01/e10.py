from Seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")
FOLDER = "sequences/"

genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gene_name in genes:
    s = Seq()
    filename = f"{gene_name}.txt"
    full_path = FOLDER + filename
    s.read_fasta(full_path) #ya hemos actualizado self.bases, para que otras funciones usen la secuencia correcta

    most_frequent = s.get_most_frequent()

    print(f"Gene {gene_name}: Most frequent Base: {most_frequent}")