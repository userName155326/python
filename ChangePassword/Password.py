import subprocess
from colorama import Fore, init

init(autoreset=True)
print(Fore.GREEN +'''[1] Change user password''')
Options = str(input("Enter your option: "))

if Options == "1":
    a = subprocess.Popen("net user",stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    print(a.stdout.read().decode("ascii"))
    #print(a.stderr)
    User = input("Enter the user: ")
    UserPassword = input("New password: ")
    print(Fore.GREEN +"The process was executed correctly.")
    a = subprocess.Popen(f"net user {User} {UserPassword}",stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    #print(a.stderr)
elif str(Options):
    print("That option is not available.")
