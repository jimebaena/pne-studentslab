import socket

PORT = 8080
IP = "212.128.255.78"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()

connection_count = 0

print(f"The Echo Server is configured on port {PORT}!")

while True:
    print("Waiting for Clients to connect...")
    (cs, client_ip_port) = ls.accept()

    connection_count += 1

    client_ip = client_ip_port[0]
    client_port = client_ip_port[1]

    print(f"Connection {connection_count} from {client_ip}, port {client_port}")

    msg_raw = cs.recv(2048)
    msg = msg_raw.decode()

    print(f"Message received: {msg}")

    response = "ECHO: " + msg

    cs.send(response.encode())

    cs.close()