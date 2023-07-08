import socket
import threading

clientes = []
green_color_code = "\033[32m"
reset_color_code = "\033[0m"

def manejar_cliente(cliente, cliente_id):
    while True:
        mensaje = cliente.recv(1024).decode()
        if mensaje == 'salir':
            break
        print(f"Cliente {cliente_id}: {mensaje}")

    cliente.close()
    clientes.remove(cliente)

def enviar_mensaje_a_todos(mensaje):
    for cliente in clientes:
        cliente.send(mensaje.encode())

def servidor():
    host = '192.168.1.39'
    port = 1234

    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, port))
    servidor_socket.listen(2)

    print("Servidor iniciado. Esperando conexiones...")

    while True:
        cliente, direccion = servidor_socket.accept()
        clientes.append(cliente)

        print(f"Cliente conectado: {direccion}")

        thread = threading.Thread(target=manejar_cliente, args=(cliente, len(clientes)))
        thread.start()

        if len(clientes) == 2:
            break

    while True:
        mensaje = input(f"[{green_color_code+'+'+reset_color_code}]Command: ")
        if mensaje == 'salir':
            break
        enviar_mensaje_a_todos(mensaje)
        

    for cliente in clientes:
        cliente.close()

    servidor_socket.close()

servidor()
