import socket

PORT = 8081
IP = "127.0.0.1"

while True:
    message = input("Message to send: ")

    if message.lower() == "exit":
        break

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((IP, PORT))
        s.send(message.encode())

        print("Message sent successfully!")

    except ConnectionRefusedError:
        print("Error: Could not connect to the server")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        s.close()