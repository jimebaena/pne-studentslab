from Client0 import Client
import socket

IP = "127.0.0.1"
PORT = 8080

for i in range(5):

    c = Client(IP, PORT)

    message = f"Message {i}"

    response = c.talk(message)

    print(f"To Server: {message}")
    print(f"From Server: {response}")
    print("")
