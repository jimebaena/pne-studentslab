import socket

# 1. Configuración: Pon AQUÍ la IP de tu ordenador (la que sale en ipconfig)
# Si estás en casa probando solo, puedes usar "127.0.0.1"
IP = "192.168.1.XX"
PORT = 8081

# 2. Crear el socket del servidor
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. "Bind": Reservar la IP y el Puerto para nosotros
ls.bind((IP, PORT))

# 4. "Listen": Empezar a escuchar (máximo 5 personas en espera)
ls.listen(5)

print(f"--- Server is ready and listening on {IP}:{PORT} ---")

while True:
    # 5. "Accept": El programa se para aquí hasta que alguien se conecta
    # conn es el cable para hablar con el cliente, addr es su dirección
    conn, addr = ls.accept()

    # 6. Recibir los datos (paquete de máximo 2048 bytes)
    data = conn.recv(2048)

    # 7. Si no nos han mandado nada, cerramos y esperamos al siguiente
    if not data:
        conn.close()
        continue

    # 8. Decodificar los bytes a texto y mostrarlo
    message = data.decode()
    print(f"Message from {addr[0]}: {message}")

    # 9. Importante: Cerrar la conexión con ese cliente concreto
    conn.close()