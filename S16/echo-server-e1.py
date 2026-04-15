import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse

PORT = 8081

socketserver.TCPServer.allow_reuse_address = True


class EchoHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        parsed_url = urlparse(self.path)
        path = parsed_url.path

        if path == "/":
            contents = Path('html/form-1.html').read_text()

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))

        elif path == "/echo":
            params = parse_qs(parsed_url.query)
            message = params.get('msg', [''])[0]

            response_html = f"""
            <!DOCTYPE html>
            <html>
            <head><title>Echo Response</title></head>
            <body>
                <h1>Received message:</h1>
                <p>{message}</p>
                <a href="/">Main Page</a>
            </body>
            </html>
            """

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(response_html)))
            self.end_headers()
            self.wfile.write(str.encode(response_html))

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
