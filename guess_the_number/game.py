import socket
import random


class NumberGuesser:
    def __init__(self):
        self.secrete_number = random.randint(1, 100)
        self.attempts = []

    def guess(self, number):
        self.attempts.append(number)

        if number == self.secrete_number:
            return "You won after " + str(len(self.attempts)) + " attempts"
        elif number > self.secrete_number:
            return "Lower"
        else:
            return "Higher"


IP = "127.0.0.1"
PORT = 8081

my_game = NumberGuesser()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversocket.bind((IP, PORT))
    serversocket.listen(5)
    print("--- Server ready in port 8081 ---")

    while True:
        (clientsocket, address) = serversocket.accept()

        data = clientsocket.recv(2048)
        if data:
            msg = data.decode("utf-8").strip()

            received_number = int(msg)

            answer = my_game.guess(received_number)

            clientsocket.send(answer.encode("utf-8"))
            print("Attempt to " + str(address) + ": " + str(received_number))

        clientsocket.close()

except socket.error:
    print("Error: The port 8081 es already being used.")
except KeyboardInterrupt:
    print("\nServer stopped.")
    serversocket.close()