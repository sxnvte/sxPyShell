import os
from colorama import Fore

version = "1.0"

print(Fore.MAGENTA + """           _____        _____ _          _ _ 
          |  __ \      / ____| |        | | |
  _____  _| |__) |   _| (___ | |__   ___| | |
 / __\ \/ /  ___/ | | |\___ \| '_ \ / _ \ | |
 \__ \>  <| |   | |_| |____) | | | |  __/ | |
 |___/_/\_\_|    \__, |_____/|_| |_|\___|_|_|
                  __/ |                      
                 |___/                       """)
print("")
print("sxPyShell v1.0 by sxnvte")
print(Fore.WHITE + "")

def custommode():
    print("spermoglwoy")

while True:
    current_directory = os.getcwd()
    command = input(f"{current_directory} $ ")

    if command == "exit":
        break

    if command == "custommode":
        custommode()

    if command.startswith("cd "):
        path = command.split(" ")[1]
        try:
            os.chdir(path)
        except FileNotFoundError:
            print(f"{path}: No such file or directory")
        continue

    os.system(command)

    

