import http.client
import json
from e2 import genes
from P02.Seq1 import Seq

SERVER = "rest.ensembl.org"
PARAMS = "?content-type=application/json"

def get_gene_info():
    conn = http.client.HTTPSConnection(SERVER)

    for gene_name in genes:
        gene_id = genes[gene_name]
        endpoint = f"/sequence/id/{gene_id}{PARAMS}"

        try:
            conn.request("GET", endpoint)
            response = conn.getresponse()

            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                sequence_str = data.get('seq')
                description = data.get('desc')

                s = Seq(sequence_str)

                print(f"\nGene: {gene_name}")
                print(f"Description: {description}")

                total_len = s.len()
                print(f"Total length: {total_len}")

                counts = s.count_base()

                for base in ["A", "C", "G", "T"]:
                    count = counts[base]
                    percentage = (count / total_len) * 100 if total_len > 0 else 0
                    print(f"  {base}: {count} ({round(percentage, 2)}%)")

                print(f"Most frequent base: {s.get_most_frequent()}")

            else:
                print(f"Error connecting to Ensembl: {response.status}")

        except Exception as e:
            print(f"An error occurred: {e}")

    conn.close()


if __name__ == "__main__":
        get_gene_info()
