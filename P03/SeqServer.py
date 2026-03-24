import socket
from P01.Seq1 import Seq

PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))
ls.listen()

print(f"Seq Server configured!")

while True:
    print("Waiting for Clients to connect...")
    (cs, client_ip_port) = ls.accept()

    msg_raw = cs.recv(2048)
    request = msg_raw.decode().strip()
    divided = request.split(" ", 1)

    info = "" #necesario para que llegue al error si por ejemplo meten "HOLA" y no de fallo porque no tenga definido esa palabra un info y command
    command = ""

    if len(divided) == 2:
        info = divided[1]
        command = divided[0]

    if request == "PING":
        print("PING command!")

        response = "OK!\n"

        print(response.strip())

        cs.send(response.encode())

    elif command == "GET":
        print("GET command!")
        if info == "0":
            response = "ACGTGACTG"
        elif info == "1":
            response = "AAAACGT"
        elif info == "2":
            response = "CCGTGAA"
        elif info == "3":
            response = "GGGTGAC"
        elif info == "4":
            response = "CCGTGA"
        else:
            response = "INVALID NUMBER"

        print(response)
        cs.send(response.encode())


    elif command == "INFO":
        print("INFO command!")
        s = Seq(info)

        length = s.len()
        counts = s.count_base()

        response = f"Total length: {length}\n"
        for base, count in counts.items():
            percentage = (count / length * 100) if length > 0 else 0
            response += f"{base}: {count} ({round(percentage, 2)}%)\n"

        cs.send(response.encode())

    elif command == "COMP":
        print("COMP command!")
        s = Seq(info)
        response = s.complement()
        cs.send(response.encode())

    elif command == "REV":
        print("REV command!")
        s = Seq(info)
        response = s.reverse()
        cs.send(response.encode())

    elif command == "GENE":
        print("GENE command!")
        FOLDER = "../sequences/"
        s = Seq()
        filename = f"{info}.txt"
        full_path = FOLDER + filename
        s.read_fasta(full_path)
        cs.send(str(s).encode()) #importante, no puedes enviar s suelto, sino con str

    else:
        error_msg = "ERROR: Command not recognized\n"
        cs.send(error_msg.encode())

    cs.close()




