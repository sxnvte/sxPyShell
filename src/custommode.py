#!/usr/bin/env python

#            _____        _____ _          _ _ 
#           |  __ \      / ____| |        | | |
#   _____  _| |__) |   _| (___ | |__   ___| | |
#  / __\ \/ /  ___/ | | |\___ \| '_ \ / _ \ | |
#  \__ \>  <| |   | |_| |____) | | | |  __/ | |
#  |___/_/\_\_|    \__, |_____/|_| |_|\___|_|_|
#                   __/ |                      
#                  |___/                       

# hi! this is a custom mode for sxPyShell you can make here your own "shell" with your commands etc. 
# please remember to set in config file customMode = True to use custom mode in sxPyShell

import os
from colorama import Fore
import sys

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
    print(f"sxPyShell by sxnvte | CUSTOM MODE")
    print("in custom mode you can make your own 'shell'. custom commands etc.")
    while True:
        command = input("sxPyShell | Custom mode > ")
        if command == "exit":
            sys.exit()