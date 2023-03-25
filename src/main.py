#!/usr/bin/env python

import os
from colorama import Fore, Style
import configparser
import time
import sys
import socket

from custommode import custommode

ver = "v1.0B"
username = os.getlogin()
hostname = socket.gethostname()

configpath = "/home/" + os.getlogin() + "/.config/sxPyShell"
if not os.path.exists(configpath):
    os.makedirs(configpath)

file_path = os.path.join(configpath, "sxPyShellConfig.ini")
if not os.path.isfile(file_path):
    print("it seems that you don`t have a config file for sxPyShell! please copy the example config from Github to the /home/username/.config/sxPyShell to continue")
    sys.exit()
config = configparser.ConfigParser()
config.read(file_path)

# if os.name == 'nt':
#     print("sxPyShell detected that you are on Windows! sxPyShell was made for Linux and on Windows it may don`t work like it supposed to be")
#     time.sleep(1.5)

# check if custom mode is enabled in config
checkCM = config.getboolean('main', 'customMode')
#prompt = config.get('main', 'prompt') disabled for now


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
print(Fore.WHITE + "" + Style.RESET_ALL)
print("type: 'sxPyShell.help to see sxPyShell commands'")

def helpcmd():
    print("Commands:")
    print("sxPyShell.info > this command will show you a information about sxPyShell")
    print("sxPyShell.reload > this command will relaod the sxPyShell")

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
    print("Creator: sxnvte")
    print("Github repository: https://github.com/sxnvte/sxPyShell")

while True:
    current_directory = os.getcwd()
    command = input(f"{username}@{hostname}:{current_directory} $ ")

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
    
    if command == "sxPyShell.help":
        print("Help for sxPyShell:")
        helpcmd()


    if command.startswith("cd "):
        path = command.split(" ")[1]
        try:
            os.chdir(path)
        except FileNotFoundError:
            print(f"{path}: No such file or directory")
        continue

    os.system(command)

    

