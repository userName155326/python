
import random
import string
import phonenumbers
from phonenumbers import geocoder
from time import sleep
from turtle import back
from colorama import Fore, init, Back

init(autoreset=True)
lksd = ['mrhacker1668','userName155326','https://github.com/userName155326']
print(Fore.GREEN+f'''
______________________________________________________
___________$b__Vb.____________________________________
___________'$b__V$b.__________________________________
____________$$b__V$$b.________________________________
____________'$$b._V$$$$oooooooo._________..___________
_____________'$$P*_V$$$$$”"**$$$b.____.o$$P___________
______________”_.oooZ$$$$b..o$$$$$$$$$$$$C____________
______________.$$$$$$$$$$$$$$$$$$$$$$$$$$$b.__________
______________$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$__________
________.o$$$o$$$$$$$$P”"*$$$$$$$$$P”"”*$$$P__________
_______.$$$**$$$$P”q$C____”$$$b________.$$P___________
_______$$P___”$$$b__”$_._.$$$$$b.______*”_____________
_______$$______$$$._____”***$$$$$$$b._A.______________
_______V$b___._Z$$b.__._______”*$$$$$b$$:_____________
________V$$.__”*$$$b.__b._________”$$$$$______________
_________”$$b_____”*$.__*b._________”$$$b_____________
___________”$$b._____”L__”$$o.________”*”_____.ooo..__
_____________”*$$o.________”*$$o.__________.o$$$$$____
_________________”*$$b._______”$$b._______.$$$$$*”____
____________________”*$$o.______”$$$o.____$$$$$'______
_______________________”$$o_______”$$$b.__”$$$$_______
_________________________”$b.______”$$$$b._”$$$$$_____
________________________._”$$_______”$$$$b__”$$$$_____
_________________________L.”$.______.$$$$$.___________
______________________________________________________
''')
print(f'''
Instagram:{lksd[0]}
Github:{lksd[1]}
Link:{lksd[2]}
 
''')
def get_country_and_region(phone_number):
    number = phonenumbers.parse(phone_number)
    country = geocoder.description_for_number(number, 'en')
    region = geocoder.region_code_for_number(number)
    return f"Region: {region}\nProvincia: {country}"

# Ejemplo de uso
phone_number = input('Ingrese el numero: ') # Número de Argentina

# Generar una dirección MAC aleatoria
mac = [0x00, 0x16, 0x3e, random.randint(0x00, 0x7f), 
       random.randint(0x00, 0xff), random.randint(0x00, 0xff)]

# Convertir la lista de números en una cadena de caracteres separada por dos puntos
mac_address = ':'.join(map(lambda x: "%02x" % x, mac))

# Generar una lista de 16 elementos (letras y números aleatorios)
random_list = [random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(16)]

# Unir los elementos en grupos de 4, separados por dos puntos
result = '::'.join([''.join(random_list[i:i+4]) for i in range(0, 16, 4)])

# Generar números aleatorios para la IP y los puertos
num1 = random.randint(100, 999)
num2 = random.randint(100, 999)
num3 = random.randint(100, 999)
num4 = random.randint(100, 999)
num_ports = random.randint(3, 37)

# Generar una lista de 10 vulnerabilidades con sus correspondientes códigos CVE y puertos
vulnerabilities = []
for i in range(random.randint(1,4)):
    # Generar código CVE aleatorio
    cve = "CVE-{}-{}".format(random.randint(2000, 2021), random.randint(10000, 99999))
    # Generar puerto aleatorio
    port = random.randint(1, 65535)
    # Agregar la vulnerabilidad a la lista
    vulnerabilities.append({"CVE": cve, "Port": port})
# Generar 15 valores aleatorios entre 00 y FF (hexadecimal)
random_values = [random.randint(0x00, 0xFF) for _ in range(15)]

# Unir los valores en una cadena separada por dos puntos
hostkey = ':'.join(map(lambda x: "{:02x}".format(x), random_values))
hostkey1 = ':'.join(map(lambda x: "{:01x}".format(x), random_values))
hostkey2 = ':'.join(map(lambda x: "{:03x}".format(x), random_values))

# Imprimir el resultado
options = ['[+]HTTP/1.0 200', '[-]HTTP/1.0 400 Bad Request']
t34t = random.choice(options)
options1 = ['[+]Request HTTPS 200', '[-]Request HTTPS 400 Bad Request']
t34t1 = random.choice(options)
options2 = ['[+]Request FTP 200', '[-]Request FTP 400 Bad Request']
t34t2 = random.choice(options)
options3 = ['[+]Request SSH 200', '[-]Request SSH 400 Bad Request']
t34t3 = random.choice(options)
# Generar coordenadas aleatorias
lat = round(random.uniform(-90, 90), 6)
lon = round(random.uniform(-180, 180), 6)
bytes1 = random.randint(13,57)
# Imprimir los resultados
ip = f"192.{num1}.{num2}.{num3}"
print("[+]Numero: ", phone_number)
print(get_country_and_region(phone_number))
print("[+]IP privada:", ip)
print("[+]Dirección MAC", mac_address)
print(f"""[+]User Agent Mozilla/{random.randint(0,10)}.{random.randint(0,10)} (X11; Linux i{random.randint(0,999)})AppleWebKit/{random.randint(0,9999)} (KHTML, like Gecko) Chrome/{random.randint(1,45)}.{random.randint(0,10)}.{random.randint(0,999)}.{random.randint(0,10)} Mobile Safari/{random.randint(0,9999)}""")
print("[+]Netmask 255.255.255.0\n[+]Broadcast 192.168.1.255")
print(t34t1)
print(t34t)
print(t34t2)
print(t34t3)
print('''[+]Content-Type: text/plain; charset=utf-8''')
print(f"""[+]DISPOSITIVOS ACTIVOS:
[HTTP] 192.168.1.{random.randint(1,255)}:80 => {ip}:80 \n[HTTP] 192.168.1.{random.randint(1,255)}:443 => {ip}:443 \n[UDP] 192.168.1.1:788 => {ip}:788 \n[TCP] 192.168.1.{random.randint(1,255)}:7777 => {ip}:345\n[TCP] 192.168.1.{random.randint(1,255)}:554 => {ip}:554""")
print("[+]IPV4:", result)
print(t34t)
print(f"[+]TX packets {random.randint(1, 999999)}  bytes {random.randint(1, 99999999)} ({random.uniform(0.01, 99.99):.2f} MB)")
print(f"[+]TX errors {random.randint(0,2)}  dropped {random.randint(1, 99999)} overruns {random.randint(0,2)}  frame {random.randint(0,2)}")
print(f"[+]RX packets {random.randint(1, 999999)}  bytes {random.randint(1, 99999999)} ({random.uniform(0.01, 99.99):.2f} MB)")
print(f"[+]RX errors {random.randint(0,2)}  dropped {random.randint(1, 39999)} overruns {random.randint(0,2)}  frame {random.randint(0,2)}")
print("[+]Coordenadas:", lat,',', lon)
print(f"[+]Zip Code: {random.randint(10000, 99999)}")
print(f'''
ssh-hostkey: 
|   2048 1b:{hostkey} (RSA)
|   521 {hostkey1} (ECDSA)
|_  126 {hostkey2} (RSA)''')
print(f"Puertos abiertos ({num_ports}):", random.sample(range(1, 65535), num_ports))
for v in vulnerabilities:
    print("[+]Vulnerabilidad: {}, Puerto: {}".format(v["CVE"], v["Port"]))
