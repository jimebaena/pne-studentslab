import http.client
import json
from e2 import genes

SERVER = "rest.ensembl.org"
GENE_NAME = "MIR633"
GENE_ID = genes[GENE_NAME]
PARAMS = "?content-type=application/json"
ENDPOINT = f"/sequence/id/{GENE_ID}{PARAMS}"

def get_gene_data():
    conn = http.client.HTTPSConnection(SERVER)

    try:
        conn.request("GET", ENDPOINT)
        response = conn.getresponse()

        print(f"Server: {SERVER}")
        print(f"URL: {SERVER}{ENDPOINT}")
        print(f"Response received!: {response.status} {response.reason}")
        print()

        if response.status == 200:
            data = json.loads(response.read().decode("utf-8"))
            print(f"Gene: {GENE_NAME}")
            print(f"Description: {data.get('desc')}")
            print(f"Bases: {data.get('seq')}")
        else:
            print(f"Error: Unexpected status code {response.status}")

    except Exception as e:
        print(f"An error occurred: {e}")

    conn.close()

if __name__ == "__main__":
    get_gene_data()