import os
from colorama import Fore
import configparser
import time
import sys

from custommode import custommode

ver = "v1.0A"

config = configparser.ConfigParser()
config.read('sxPyShellConfig.ini')

if os.name == 'nt':
    print("sxPyShell detected that you are on Windows! sxPyShell was made for Linux and on Windows it may don`t work like it supposed to be")

time.sleep(1.5)

# check if custom mode is enabled in config
checkCM = config.getboolean('main', 'customMode')

def custommode():
    print(Fore.MAGENTA + """           _____        _____ _          _ _ 
          |  __ \      / ____| |        | | |
  _____  _| |__) |   _| (___ | |__   ___| | |
 / __\ \/ /  ___/ | | |\___ \| '_ \ / _ \ | |
 \__ \>  <| |   | |_| |____) | | | |  __/ | |
 |___/_/\_\_|    \__, |_____/|_| |_|\___|_|_|
                  __/ |                      
                 |___/                       """)
    print(Fore.WHITE + "")
    print(f"sxPyShell {ver} CUSTOM MODE by sxnvte")
    print("in custom mode you can make own 'shell'. custom commands etc.")
    while True:
        command = input("sxPyShell | Custom mode > ")

if checkCM == True:
    custommode()

print(Fore.MAGENTA + """           _____        _____ _          _ _ 
          |  __ \      / ____| |        | | |
  _____  _| |__) |   _| (___ | |__   ___| | |
 / __\ \/ /  ___/ | | |\___ \| '_ \ / _ \ | |
 \__ \>  <| |   | |_| |____) | | | |  __/ | |
 |___/_/\_\_|    \__, |_____/|_| |_|\___|_|_|
                  __/ |                      
                 |___/                       """)
print("")
print(f"sxPyShell {ver} by sxnvte")
print(Fore.WHITE + "")

def info():
    print(Fore.MAGENTA + """           _____        _____ _          _ _ 
          |  __ \      / ____| |        | | |
  _____  _| |__) |   _| (___ | |__   ___| | |
 / __\ \/ /  ___/ | | |\___ \| '_ \ / _ \ | |
 \__ \>  <| |   | |_| |____) | | | |  __/ | |
 |___/_/\_\_|    \__, |_____/|_| |_|\___|_|_|
                  __/ |                      
                 |___/                       """)
    print("")
    print(Fore.WHITE + "")
    print(f"Version: {ver}")
    print("Author: sxnvte")
    print("Github repository: https://github.com/sxnvte/sxPyShell")

while True:
    current_directory = os.getcwd()
    command = input(f"{current_directory} $ ")

    if command == "exit":
        break

    if command == "custommode":
        custommode()

    if command == "sxPyShell.info":
        info()

    if command == "sxPyShell.reload":
        print("reloading sxPyShell")
        time.sleep(0.5)
        os.system("clear")
        python = sys.executable
        os.execl(python, python, *sys.argv)


    if command.startswith("cd "):
        path = command.split(" ")[1]
        try:
            os.chdir(path)
        except FileNotFoundError:
            print(f"{path}: No such file or directory")
        continue

    os.system(command)

    

