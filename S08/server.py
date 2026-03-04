import socket

IP = "127.0.0.1"
PORT = 8081
MAX_OPEN_REQUESTS = 5

# Counter for tracking how many people connected
number_con = 0

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Bind the socket to your specific IP and Port
    serversocket.bind((IP, PORT))

    # Start listening for incoming connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    print(f"--- Server is running at {IP}:{PORT} ---")

    while True:
        print("Waiting for a new connection...")
        (clientsocket, address) = serversocket.accept()

        # Increment connection counter
        number_con += 1
        print(f"CONNECTION {number_con}: Received from {address}")

        data = clientsocket.recv(2048)
        message = data.decode("utf-8")
        print(f"Client says: {message}")

        response = "Hello! I have received your message successfully.\n"
        clientsocket.send(response.encode("utf-8"))

        clientsocket.close()
        print(f"Connection {number_con} closed.\n")

except socket.error:
    print(f"Error: Could not use IP {IP} or Port {PORT}. Check your IP address!")

except KeyboardInterrupt:
    print("\nServer stopped by the user.")
    serversocket.close()