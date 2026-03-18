import socket
import termcolor

IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    lines = req.split('\n')

    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    body = """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Holaaa</title>
      </head>
      <body style="background-color: turquoise;">
        <h1>Me salgo de la carrera</h1>
        <p>I am the Green Server! :-)</p>
      </body>
    </html>
    """

    status_line = "HTTP/1.1 200 OK\n"

    header = "Content-Type: text/plain\n"

    header += f"Content-Length: {len(body)}\n"

    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()

print("Green server configured!")

while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:

        process_client(cs)

        cs.close()
