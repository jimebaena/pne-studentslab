import http.server
import socketserver
import requests
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


class GenomeHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        contents = ""

        if path == "/":
            contents = Path('html/index.html').read_text()
            self.send_response(200)

        elif path == "/listSpecies":
            params = parse_qs(parsed_url.query)
            limit_val = params.get('limit', [''])[0]

            url = "https://rest.ensembl.org/info/species"
            try:
                response = requests.get(url, headers={"Content-Type": "application/json"})
                if response.status_code == 200:
                    data = response.json()
                    all_species = data['species']
                    total_species = len(all_species)

                    names = []
                    for s in all_species:
                        names.append(s['display_name'])

                    if limit_val and limit_val != "":
                        names = names[:int(limit_val)]
                        display_limit = limit_val
                    else:
                        display_limit = "All"

                    especies_html = ""
                    for n in names:
                        especies_html += f"<li>{n}</li>"

                    template = read_html_file("list.html")
                    contents = template.render(info={
                        "list": especies_html,
                        "total": total_species,
                        "limit": display_limit
                    })
                    self.send_response(200)
                else:
                    self.send_response(404)
                    contents = Path('html/error.html').read_text()

            except Exception as e:
                contents = f"<h1>Internal Error: {e}</h1>"
                self.send_response(500)


        elif path == "/karyotype":
            params = parse_qs(parsed_url.query)
            species = params.get('species', [''])[0]

            if not species:
                self.send_response(404)
                contents = Path('html/error.html').read_text()
            else:
                url = f"https://rest.ensembl.org/info/assembly/{species.replace(' ', '%20')}"

                try:
                    response = requests.get(url, headers={"Content-Type": "application/json"})

                    if response.status_code == 200:
                        data = response.json()

                        karyotypes = data.get('karyotype', [])

                        karyotype_html = ""
                        for chromo in karyotypes:
                            karyotype_html += f"<li>{chromo}</li>"

                        template = read_html_file("karyotype.html")
                        contents = template.render(info={
                            "list": karyotype_html
                        })
                        self.send_response(200)
                    else:
                        self.send_response(404)
                        contents = Path('html/error.html').read_text()

                except Exception as e:
                    self.send_response(500)
                    contents = f"<h1>Internal Error: {e}</h1>"


        elif path == "/chromosomeLength":
            params = parse_qs(parsed_url.query)
            species = params.get('species', [''])[0]
            chromo = params.get('chromo', [''])[0]

            if not species or not chromo:
                self.send_response(404)
                contents = Path('html/error.html').read_text()

            else:
                url = f"https://rest.ensembl.org/info/assembly/{species.replace(" ", "%20")}"
                try:
                    response = requests.get(url, headers={"Content-Type": "application/json"})

                    if response.status_code == 200:
                        data = response.json()
                        regions = data.get('top_level_region', [])

                        found_length = ""

                        for region in regions:
                            if region.get('name') == chromo and region.get('coord_system') == 'chromosome':
                                found_length = region.get('length')

                        if found_length != "":
                            template = read_html_file("chromolength.html")
                            contents = template.render(info={
                                "length": found_length
                            })
                            self.send_response(200)
                        else:
                            self.send_response(404)
                            contents = Path('html/error.html').read_text()
                    else:
                        self.send_response(404)
                        contents = Path('html/error.html').read_text()

                except Exception as e:
                    self.send_response(500)
                    contents = f"<h1>Internal Error: {e}</h1>"


        elif path == "/geneLookup":
            params = parse_qs(parsed_url.query)
            gene_name = params.get('gene', [''])[0]

            if not gene_name:
                self.send_response(404)
                contents = Path('html/error.html').read_text()
            else:
                url = f"https://rest.ensembl.org/lookup/symbol/homo_sapiens/{gene_name}"

                try:
                    response = requests.get(url, headers={"Content-Type": "application/json"})

                    if response.status_code == 200:
                        data = response.json()

                        ensembl_id = data.get('id')

                        template = read_html_file("genelookup.html")
                        contents = template.render(info={
                            "gene": gene_name,
                            "id": ensembl_id
                        })
                        self.send_response(200)
                    else:
                        self.send_response(404)
                        contents = Path('html/error.html').read_text()

                except Exception as e:
                    self.send_response(500)
                    contents = f"<h1>Internal Error: {e}</h1>"

        elif path == "/geneSeq":
            params = parse_qs(parsed_url.query)
            gene_name = params.get('gene', [''])[0]

            if not gene_name:
                self.send_response(404)
                contents = Path('html/error.html').read_text()
            else:
                url = f"https://rest.ensembl.org/lookup/symbol/homo_sapiens/{gene_name}"

                try:
                    response = requests.get(url, headers={"Content-Type": "application/json"})

                    if response.status_code == 200:
                        data = response.json()
                        ensembl_id = data.get('id')

                        url2 = f"https://rest.ensembl.org/sequence/id/{ensembl_id}"
                        response2 = requests.get(url2, headers={"Content-Type": "application/json"})
                        data2 = response2.json()
                        seq = data2.get("seq")
                        template = read_html_file("geneseq.html")
                        contents = template.render(info={
                            "gene": gene_name,
                            "seq": seq
                        })
                        self.send_response(200)

                    else:
                        self.send_response(404)
                        contents = Path('html/error.html').read_text()

                except Exception as e:
                    self.send_response(500)
                    contents = f"<h1>Internal Error: {e}</h1>"

        elif path == "/geneInfo":
            params = parse_qs(parsed_url.query)
            gene_name = params.get('gene', [''])[0]

            if not gene_name:
                self.send_response(404)
                contents = Path('html/error.html').read_text()
            else:
                url = f"https://rest.ensembl.org/lookup/symbol/homo_sapiens/{gene_name}"

                try:
                    response = requests.get(url, headers={"Content-Type": "application/json"})

                    if response.status_code == 200:
                        data = response.json()
                        ensembl_id = data.get('id')

                        url2 = f"https://rest.ensembl.org/lookup/id/{ensembl_id}"
                        response2 = requests.get(url2, headers={"Content-Type": "application/json"})

                        data2 = response2.json()
                        start = data2.get("start")
                        end = data2.get("end")
                        identifier = data2.get("id")
                        chr_name = data2.get("seq_region_name")
                        length = int(end) - int(start)

                        template = read_html_file("geneinfo.html")
                        contents = template.render(info={
                            "gene_name": gene_name,
                            "chr_name": chr_name,
                            "id": identifier,
                            "start": start,
                            "end": end,
                            "length": length
                        })
                        self.send_response(200)

                    else:
                        self.send_response(404)
                        contents = Path('html/error.html').read_text()

                except Exception as e:
                    self.send_response(500)
                    contents = f"<h1>Internal Error: {e}</h1>"

        elif path == "/geneCalc":
            params = parse_qs(parsed_url.query)
            gene_name = params.get('gene', [''])[0]

            if not gene_name:
                self.send_response(404)
                contents = Path('html/error.html').read_text()
            else:
                url = f"https://rest.ensembl.org/lookup/symbol/homo_sapiens/{gene_name}"

                try:
                    response = requests.get(url, headers={"Content-Type": "application/json"})

                    if response.status_code == 200:
                        data = response.json()
                        ensembl_id = data.get('id')

                        url2 = f"https://rest.ensembl.org/sequence/id/{ensembl_id}"
                        response2 = requests.get(url2, headers={"Content-Type": "application/json"})
                        data2 = response2.json()
                        clean_seq = data2.get("seq")
                        length = len(clean_seq)
                        bases = {"A": 0, "T": 0, "C": 0, "G": 0}
                        for t in clean_seq:
                            if t in bases:
                                bases[t] += 1

                        adenine = round((bases["A"] / length) * 100, 2)
                        thymine = round((bases["T"] / length) * 100, 2)
                        cytosine = round((bases["C"] / length) * 100, 2)
                        guanine = round((bases["G"] / length) * 100, 2)

                        template = read_html_file("genecalc.html")
                        contents = template.render(info={
                            "gene": gene_name,
                            "length": length,
                            "adenine": adenine,
                            "thymine": thymine,
                            "cytosine": cytosine,
                            "guanine": guanine
                        })
                        self.send_response(200)

                    else:
                        self.send_response(404)
                        contents = Path('html/error.html').read_text()

                except Exception as e:
                    self.send_response(500)
                    contents = f"<h1>Internal Error: {e}</h1>"

        elif path == "/geneList":
            params = parse_qs(parsed_url.query)
            chromo = params.get('chromo', [''])[0]
            start = params.get('start', [''])[0]
            end = params.get('end', [''])[0]

            if not chromo or not start or not end:
                self.send_response(404)
                contents = Path('html/error.html').read_text()
            else:
                url = f"https://rest.ensembl.org/overlap/region/human/{chromo}:{start}-{end}?feature=gene;feature=transcript;feature=cds;feature=exon;"

                try:
                    response = requests.get(url, headers={"Content-Type": "application/json"})

                    if response.status_code == 200:
                        data = response.json()

                        gene_names = []
                        for dic in data:
                            gene_names.append({dic.get("external_name", "No Name"): dic.get("id")})

                        genes_html = ""
                        for dic in gene_names:
                            for k, v in dic.items():
                                genes_html += f"<li>{k}: {v}</li>"

                        template = read_html_file("geneList.html")
                        contents = template.render(info={
                            "genes_names": genes_html,
                            "chromo": chromo
                        })
                        self.send_response(200)

                    else:
                        self.send_response(404)
                        contents = Path('html/error.html').read_text()

                except Exception as e:
                    self.send_response(500)
                    contents = f"<h1>Internal Error: {e}</h1>"

        elif path == "/chromosomesSorted":

            url = f"https://rest.ensembl.org/info/assembly/homo_sapiens"

            try:
                response = requests.get(url, headers={"Content-Type": "application/json"})

                if response.status_code == 200:
                    data = response.json()

                    karyotypes = data.get('karyotype', [])

                    numeric = []
                    for chromo in karyotypes:
                        if chromo.isdigit():
                            numeric.append(int(chromo))

                    ordered = sorted(numeric, reverse=True)

                    karyotype_html = ""
                    for chromo in ordered:
                        karyotype_html += f"<li>{chromo}</li>"

                    template = read_html_file("chromosorted.html")
                    contents = template.render(info={
                        "list": karyotype_html
                    })
                    self.send_response(200)
                else:
                    self.send_response(404)
                    contents = Path('html/error.html').read_text()

            except Exception as e:
                self.send_response(500)
                contents = f"<h1>Internal Error: {e}</h1>"

        elif path == "/sequenceSearch":
            params = parse_qs(parsed_url.query)
            gene_name = params.get('gene', [''])[0]
            pattern = params.get('pattern', [''])[0]

            if not gene_name or not pattern:
                self.send_response(404)
                contents = Path('html/error.html').read_text()
            else:
                url = f"https://rest.ensembl.org/lookup/symbol/homo_sapiens/{gene_name}"

                try:
                    response = requests.get(url, headers={"Content-Type": "application/json"})

                    if response.status_code == 200:
                        data = response.json()
                        ensembl_id = data.get('id')

                        url2 = f"https://rest.ensembl.org/sequence/id/{ensembl_id}"
                        response2 = requests.get(url2, headers={"Content-Type": "application/json"})
                        data2 = response2.json()
                        clean_seq = data2.get("seq")
                        length = len(clean_seq)
                        total = clean_seq.count(pattern)

                        template = read_html_file("seqsearch.html")
                        contents = template.render(info={
                            "gene": gene_name,
                            "pattern": pattern,
                            "length": length,
                            "total": total
                        })
                        self.send_response(200)

                    else:
                        self.send_response(404)
                        contents = Path('html/error.html').read_text()

                except Exception as e:
                    self.send_response(500)
                    contents = f"<h1>Internal Error: {e}</h1>"

        elif path == "/longGenes":
            params = parse_qs(parsed_url.query)
            chromo = params.get('chromo', [''])[0]
            start = params.get('start', [''])[0]
            end = params.get('end', [''])[0]
            min_length = params.get('min', [''])[0]

            if not chromo or not start or not end or not min_length:
                self.send_response(404)
                contents = Path('html/error.html').read_text()
            else:
                url = f"https://rest.ensembl.org/overlap/region/human/{chromo}:{start}-{end}?feature=gene;feature=transcript;feature=cds;feature=exon;"

                try:
                    response = requests.get(url, headers={"Content-Type": "application/json"})

                    if response.status_code == 200:
                        data = response.json()

                        gene_names = []
                        for dic in data:
                            length = int(dic.get("end")) - int(dic.get("start"))
                            if length >= int(min_length):
                                gene_names.append({dic.get("external_name", "No Name"): dic.get("id")})

                        genes_html = ""
                        for dic in gene_names:
                            for k, v in dic.items():
                                genes_html += f"<li>{k}: {v}</li>"

                        template = read_html_file("longgenes.html")
                        contents = template.render(info={
                            "genes_names": genes_html,
                            "chromo": chromo
                        })
                        self.send_response(200)

                    else:
                        self.send_response(404)
                        contents = Path('html/error.html').read_text()

                except Exception as e:
                    self.send_response(500)
                    contents = f"<h1>Internal Error: {e}</h1>"

        else:
            try:
                contents = Path('html/error.html').read_text()
            except FileNotFoundError:
                contents = "<h1>404 Not Found</h1><p>Error page missing too!</p>"

            self.send_response(404)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))

with socketserver.TCPServer(("", PORT), GenomeHandler) as httpd:
    print(f"Serving at PORT {PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()