import requests

BASE_URL = "http://localhost:8080"


def test_list_species():
    limit = input("Enter species limit (or press Enter for all): ").strip()
    url = f"{BASE_URL}/listSpecies?limit={limit}&json=1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\n--- Species List (Total Tracked: {data['total']}, Showing: {data['limit']}) ---")
            for species in data['species']:
                print(f" * {species}")
        else:
            print(f"Server Error status: {response.status_code}")
    except Exception as e:
        print(f"Connection breakdown: {e}")


def test_karyotype():
    species = input("Enter species identifier (e.g., human): ").strip()
    url = f"{BASE_URL}/karyotype?species={species}&json=1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\n--- Karyotype Data for {data['species'].upper()} ---")
            print(f"Chromosomes found: {', '.join(data['karyotype'])}")
        else:
            print(f"Species data unresolved on server (Code {response.status_code}).")
    except Exception as e:
        print(f"Connection breakdown: {e}")


def test_chromosome_length():
    species = input("Enter target species (e.g., human): ").strip()
    chromo = input("Enter chromosome token (e.g., 1): ").strip()
    url = f"{BASE_URL}/chromosomeLength?species={species}&chromo={chromo}&json=1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\n--- Coordinate Scale Output ---")
            print(f"Species Context: {data['species']}")
            print(f"Chromosome Target: {data['chromo']}")
            print(f"Total Structural Base Pairs: {data['length']} bp")
        else:
            print(f"Data entry invalid or missing reference (Code {response.status_code}).")
    except Exception as e:
        print(f"Connection breakdown: {e}")


def test_gene_lookup():
    gene = input("Enter target symbol matrix (e.g., BRCA2): ").strip()
    url = f"{BASE_URL}/geneLookup?gene={gene}&json=1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\n--- Map Identity Results ---")
            print(f"Symbol Entry: {data['gene']}")
            print(f"Ensembl Stable Identity: {data['id']}")
        else:
            print(f"Symbol sequence unresolved (Code {response.status_code}).")
    except Exception as e:
        print(f"Connection breakdown: {e}")


def test_gene_seq():
    gene = input("Enter gene symbol for sequence recovery (e.g., FRAT2): ").strip()
    url = f"{BASE_URL}/geneSeq?gene={gene}&json=1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\n--- Sequence Acquisition Results ---")
            print(f"Gene Symbol: {data['gene']}")
            print(f"Ensembl ID: {data['id']}")
            print(f"Sequence Preview: {data['seq'][:60]}...")
        else:
            print(f"Sequence unavailable or symbol incorrect (Code {response.status_code}).")
    except Exception as e:
        print(f"Connection breakdown: {e}")


def test_gene_info():
    gene = input("Enter gene symbol for operational metadata (e.g., FRAT2): ").strip()
    url = f"{BASE_URL}/geneInfo?gene={gene}&json=1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\n--- Gene Structural Metadata ---")
            print(f"Gene Name: {data['gene_name']}")
            print(f"Chromosome Location: {data['chr_name']}")
            print(f"Ensembl ID: {data['id']}")
            print(f"Coordinates: Start {data['start']} | End {data['end']}")
            print(f"Calculated Span: {data['length']} bp")
        else:
            print(f"Metadata could not be computed (Code {response.status_code}).")
    except Exception as e:
        print(f"Connection breakdown: {e}")


def test_gene_calc():
    gene = input("Enter gene symbol for base calculation (e.g., FRAT2): ").strip()
    url = f"{BASE_URL}/geneCalc?gene={gene}&json=1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\n--- Nucleotide Base Calculations ---")
            print(f"Target Gene: {data['gene']}")
            print(f"Sequence Length: {data['length']} nucleotides")
            print(f"Adenine (A): {data['adenine']}%")
            print(f"Thymine (T): {data['thymine']}%")
            print(f"Cytosine (C): {data['cytosine']}%")
            print(f"Guanine (G): {data['guanine']}%")
        else:
            print(f"Calculations aborted by server (Code {response.status_code}).")
    except Exception as e:
        print(f"Connection breakdown: {e}")


def test_gene_list():
    chromo = input("Enter target chromosome (e.g., 1): ").strip()
    start = input("Enter start coordinate boundary: ").strip()
    end = input("Enter end coordinate boundary: ").strip()
    url = f"{BASE_URL}/geneList?chromo={chromo}&start={start}&end={end}&json=1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\n--- Region Mapping Results ({data['chromo']}:{data['start']}-{data['end']}) ---")
            print(f"Total overlapping features matched: {len(data['genes'])}")
            for item in data['genes'][:10]:  # Limits preview logs to top 10 rows
                print(f" * Symbol: {item['name']} | ID: {item['id']}")
        else:
            print(f"Region scanning rejected by server (Code {response.status_code}).")
    except Exception as e:
        print(f"Connection breakdown: {e}")


def main():
    running = True
    while running:
        print("\n" + "=" * 35)
        print("    REST API REMOTE CLIENT ENGINE    ")
        print("=" * 35)
        print("1. Query Species List")
        print("2. Pull Karyotype Metrics")
        print("3. Read Chromosome Length")
        print("4. Execute Gene Lookup")
        print("5. Extract Gene Sequence")
        print("6. Fetch Gene Info Mapping")
        print("7. Process Base Percentage Calc")
        print("8. Scan Region Overlap Gene List")
        print("9. Exit Session")

        choice = input("\nSelect directive (1-9): ").strip()

        if choice == "1":
            test_list_species()
        elif choice == "2":
            test_karyotype()
        elif choice == "3":
            test_chromosome_length()
        elif choice == "4":
            test_gene_lookup()
        elif choice == "5":
            test_gene_seq()
        elif choice == "6":
            test_gene_info()
        elif choice == "7":
            test_gene_calc()
        elif choice == "8":
            test_gene_list()
        elif choice == "9":
            print("\nShutting down client. Goodbye.")
            running = False
        else:
            print("\nInvalid index. Please input 1-9.")


if __name__ == "__main__":
    main()