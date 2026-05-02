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