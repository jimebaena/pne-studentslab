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
            try:
                contents = Path('html/form-e2.html').read_text(encoding='utf-8')
                self.send_response(200)
            except FileNotFoundError:
                contents = "<h1>Error: html/form-e1.html not found</h1>"
                self.send_response(404)


        elif self.path.startswith("/echo"):
            try:
                message = self.path.split("=")[1]
                message = message.replace("+", " ")
            except IndexError:
                message = "No message received"

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

        else:
            try:
                contents = Path('html/error.html').read_text(encoding='utf-8')
            except FileNotFoundError:
                contents = "<h1>404 Not Found</h1><a href='/'>Back to Home</a>"
            self.send_response(404)

        payload = str.encode(contents)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(payload))
        self.end_headers()
        self.wfile.write(payload)

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at PORT {PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()