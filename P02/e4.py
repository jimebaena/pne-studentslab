from Client0 import Client

PRACTICE = 2
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8081
FOLDER = "sequences/"

genes_to_send = ["U5", "FRAT1", "ADA"]

c = Client(IP, PORT)

for gene_name in genes_to_send:
    s = Client()
    filename = f"{gene_name}.txt"
    full_path = FOLDER + filename

    try:
        s.read_fasta(full_path)

        print(f"Sending the {gene_name} Gene to the server...")

        # Enviamos la secuencia al servidor
        # str(s) convierte tu objeto Seq en la cadena de bases (A, C, T, G)
        response = c.talk(str(s))

        print(f"Response: {response}")

    except FileNotFoundError:
        print(f"Error: No se encuentra el archivo en {full_path}")

print("\nAll genes sent successfully!")