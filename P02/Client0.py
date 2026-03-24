import socket

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("OK!")

    def __str__(self):
        return f"Connection to SERVER at {self.ip}, PORT: {self.port}"

    def talk(self, msg):
        # Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Establish connection using the stored IP and Port
        s.connect((self.ip, self.port))

        # Send the message (encoded to bytes)
        s.send(msg.encode("utf-8"))

        # Receive the response
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        return response

