import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8081

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        if self.path == "/":
            contents = Path('html/form-1.html').read_text()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))

        elif self.path.startswith("/echo"):
            try:
                message = self.path.split("=")[1]
                message = message.replace("+", " ")
            except IndexError:
                message = ""

            contents = f"""
            <!DOCTYPE html>
            <html>
            <head><meta charset="utf-8"></head>
            <body>
                <h1>Echo Server</h1>
                <p>The sent message is: <b>{message}</b></p>
                <hr>
                <a href="/">Main Page</a>
            </body>
            </html>
            """
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))

        else:
            contents = Path('html/error.html').read_text()
            self.send_response(404)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))

        return

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()