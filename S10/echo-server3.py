import socket

PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()

clients_list = []

print("The server is configured!")

while len(clients_list) < 5:
    print("Waiting for Clients to connect")
    (cs, client_ip_port) = ls.accept()

    clients_list.append(client_ip_port)

    msg_raw = cs.recv(2048)
    msg = msg_raw.decode()


    print(f"CONNECTION {len(clients_list)}. Client IP,PORT: {client_ip_port}")
    print(f"Message received: {msg.strip()}")

    response = "ECHO: " + msg
    cs.send(response.encode())

    cs.close()

print("Limit reached. The clients that have connected are: ")

for i in range(len(clients_list)):
    print(f"Client {i}: {clients_list[i]}")

ls.close()
