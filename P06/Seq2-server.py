import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

PORT = 8081

socketserver.TCPServer.allow_reuse_address = True


class EchoHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        parsed_url = urlparse(self.path)
        path = parsed_url.path

        if path == "/":
            contents = Path('html/index.html').read_text()

            self.send_response(200)

        elif path == "/ping":
            contents = f"""
            <!DOCTYPE html>
            <html>
            <head><title>Ping</title></head>
            <body>
                <h1>PING OK!</h1>
                <p>The SEQ2 server is running...</p>
                <p><a href="/">Main page</a></p>
            </body>
            </html>
            """


            self.send_response(200)

        elif path == "/get":
            params = parse_qs(parsed_url.query)
            try:
                message = params.get('number', [''])[0]
                n = int(message)

                sequences = {
                    0: "ACGTGAGTGCGTA",
                    1: "AAAACCTGTAAAG",
                    2: "CCCCCGTTGGGA",
                    3: "GGGTTTTCAGT",
                    4: "CGTGACAAGTCCGTA"
                }

                seq = sequences.get(n, "Seq not found")

                def read_html_file(filename):
                    contents = Path("html/" + filename).read_text()
                    contents = j.Template(contents)
                    return contents

                contents = read_html_file("get.html").render(info={"seq" : seq, "num" : n})
                self.send_response(200)


            except (ValueError, IndexError):
                contents = "Error: Introduce a valid number."
                self.send_response(404)

        elif path == "/gene":
            params = parse_qs(parsed_url.query)
            gene_name = params.get('genes', [''])[0]

            gene_path = Path(f"../sequences/{gene_name}.txt")
            sequence = gene_path.read_text()

            def read_html_file(filename):
                contents = Path("html/" + filename).read_text()
                contents = j.Template(contents)
                return contents

            template = read_html_file("gene.html")
            contents = template.render(info={"name": gene_name, "seq": sequence})

            self.send_response(200)

        elif path == "/operation":
            params = parse_qs(parsed_url.query)
            seq = params.get('msg', [''])[0].upper()
            op = params.get('operation', [''])[0]

            result = ""
            length = len(seq)

            valid = "ACGT"
            total = 0

            for base in seq:
                if base in valid:
                    total += 1
            if total != length:
                result = "Invalid sequence"

            elif op == "Info":
                if length > 0:
                    a = seq.count('A')
                    c = seq.count('C')
                    g = seq.count('G')
                    t = seq.count('T')

                    p_a = (a / length) * 100
                    p_c = (c / length) * 100
                    p_g = (g / length) * 100
                    p_t = (t / length) * 100

                    result = (f"Total length: {length} <br> "
                              f"A: {a} ({p_a:.1f}%) <br> "
                              f"C: {c} ({p_c:.1f}%) <br> "
                              f"G: {g} ({p_g:.1f}%) <br> "
                              f"T: {t} ({p_t:.1f}%) <br>")
                else:
                    result = "Empty sequence"

            elif op == "Comp":
                complement_seq = ""
                for base in seq:
                    if base == 'A':
                        complement_seq += 'T'
                    elif base == 'T':
                        complement_seq += 'A'
                    elif base == 'C':
                        complement_seq += 'G'
                    elif base == 'G':
                        complement_seq += 'C'

                result = complement_seq
            elif op == "Rev":
                result = seq[::-1]

            def read_html_file(filename):
                contents = Path("html/" + filename).read_text()
                return j.Template(contents)

            template = read_html_file("operation.html")
            contents = template.render(info={
                "seq": seq,
                "op": op,
                "res": result
            })
            self.send_response(200)

        else:
            contents = Path('html/error.html').read_text()

            self.send_response(404)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))
        return


Handler = EchoHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at PORT {PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()