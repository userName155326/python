import nmap
import scapy.all as scapy
import colorama
import timeit
from datetime import datetime

PACKETS1 = int(input('Packet limits: '))
# Initialize colorama
colorama.init(autoreset=True)
correct = colorama.Fore.GREEN + "[+]"
wait = colorama.Fore.YELLOW + "[*]"
failed = colorama.Fore.RED + "[-]"

def detect_dos():
    # Track the number of packets in the last 10 seconds
    packets = scapy.sniff(timeout=10)
    if len(packets) > 1000:
        # Send an alert if a large number of incoming packets are detected
        print(f"{failed} DoS attack detected! ({len(packets)} packets received)")
        # Attacker's IP address details
        print(f"{failed} Attacker's IP address: {packets[0].src}")
    else:
        print(f"{correct} No signs of a DoS attack detected")

# Create an nmap port scanning object
nm = nmap.PortScanner()

# Known IP dictionary
known_ips = {}
count = 0

# Welcome message and explanation
print("Scanning the local network to detect devices...")
print(f"This script can also detect DoS attacks with more than {PACKETS1} packets received in the last 10 seconds.\n")

while True:
    # Scan the local network to find devices
    nm.scan(hosts='192.168.1.0/24', arguments='-sP')

    # Iterate over each detected host
    for ip in nm.all_hosts():
        try:
            # Check if the IP is new
            if ip not in known_ips:
                now = datetime.now()
                count += 1
                time_now = now.strftime("%H:%M:%S")
                print(f"{wait} [{count}][{time_now}] Detected IP: {ip}")
                known_ips[ip] = now

            # Check if the IP has disconnected
            elif nm[ip].state() == 'down':
                print(f"IP disconnected: {ip}")
                known_ips.pop(ip, None)

        except Exception as e:
            print(f"Error processing IP address: {e}")

    detect_dos()
