import socket
import termcolor

IP = "127.0.0.1"
PORT = 8081

termcolor.cprint("--- Welcome to the Number Guessing Game! ---", "yellow")

game_over = False

while not game_over:
    try:
        user_input = input("\nEnter your guess (0-100): ")

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((IP, PORT))

        client_socket.send(user_input.encode("utf-8"))

        response = client_socket.recv(2048).decode("utf-8")

        if "Higher" == response:
            termcolor.cprint("Hint: Higher!", "red")
        elif "Lower" == response:
            termcolor.cprint("Hint: Lower!", "blue")
        else:
            termcolor.cprint("★ " + response + " ★", "green")
            game_over = True

        client_socket.close()

    except ValueError:
        print("Please enter a valid integer.")
    except ConnectionRefusedError:
        print("Error: Could not connect.")
        break
    except KeyboardInterrupt:
        print("\nClosing the game...")
        break

print("--- Game Finished ---")