# ALL IMPORT

import time
import os
import pystyle
import colorama
import colored
import smtplib
import requests
import platform
import sys
import webbrowser
from tqdm import tqdm
from colored import *
from pystyle import Colors, Colorate
from colorama import *


# CLEAR


if platform.system().startswith("Linux"):
    os.system('clear')
elif platform.system().startswith("Windows"):
    os.system('cls')


# WAIT


print(f"{Fore.RED}[", end=''), print(f'{colored.fg(172)}+', end=''), print(f"{Fore.RED}]", end=''), print(f'{colored.fg(172)} Please Wait ')


# ASCII 1



time.sleep(1)


amd = (Colorate.Horizontal(Colors.red_to_yellow,"""

                      ,-,-      
                     / / |      
   ,-'             _/ / /       
  (-_          _,-' `Z_/        
   "#:      ,-'_,-.    \  _     
    #'    _(_-'_()\     \" |    
  ,--_,--'                 |    
 / ""                      L-'\ 
 \,--^---v--v-._        /   \ | 
   \_________________,-'      | 
                    \          \ 
                     \          /
       Loading...     \          /


"""))


print("")
print("")
print("")
print("")


for char in amd:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.00000234)


time.sleep(2)


for i in tqdm(range(int(9e6))):
    pass


# CLEAR


if platform.system().startswith("Linux"):
    os.system('clear')
elif platform.system().startswith("Windows"):
    os.system('cls')
    

# WAIT


print(f"{Fore.RED}[", end=''), print(f'{colored.fg(172)}+', end=''), print(f"{Fore.RED}]", end=''), print(f'{colored.fg(172)} Please Wait ')


# CLEAR


if platform.system().startswith("Linux"):
    os.system('clear')
elif platform.system().startswith("Windows"):
    os.system('cls')


# ASCII  2

print(Fore.CYAN + "  ____   ___  ____  ____   __   _  _      ____  _  _  ____ ")
print(Colors.red, "/ ___) / __)(  _ \(  __) / _\ ( \/ )    (_  _)( \/ )(  _ /")
print(Colors.orange, "\___ \( (__  )   / ) _) /    \/ \/ \      )(   )  (  )   /")
print(Fore.BLUE + " (____/ \___)(__\_)(____)\_/\_/\_)(_/     (__) (_/\_)(__\_)")
print(f"{Fore.YELLOW}                                                  [{Fore.BLUE}v.12345{Fore.YELLOW}] ")
print(f"{Fore.LIGHTBLUE_EX}                                                [{Fore.RED}By {Fore.CYAN}Newark{Fore.LIGHTBLUE_EX}] ")
print("")
print("")
print("")
print("")


# CATEGORY


print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}01', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}DDoS ')
print("")
print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}02', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Spamming ')
print("")
print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}03', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Port Scanner ')
print("")
print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}04', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}DoXxing ')
print("")
print("")
print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}0', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Exit ', end=''), print("                ", end=''), print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}9', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Github ', end=''),print("                ", end=''), print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}h', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Help ')
print("      ")
print("      ")
print("      ")

print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}?', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Please choose an option ')

option = int(input("> "))


# OPTION 1

if option == 1:
    if platform.system().startswith("Linux"):
        os.system('clear')
    elif platform.system().startswith("Windows"):
        os.system('cls')

    time.sleep(1.25)

    if platform.system().startswith("Linux"):
        os.system('python3 tcpdos.py')
    elif platform.system().startswith("Windows"):
        import tcpdos


# OPTION 2


if option == 2:
     print(f"{Fore.RED}[", end=''), print(f'{colored.fg(172)}+', end=''), print(f"{Fore.RED}]", end=''), print(f'{colored.fg(172)} Please Wait ')
    
     time.sleep(3)
     if platform.system().startswith("Linux"):
        os.system('clear')
        os.system('python3 parcel.py')
     elif platform.system().startswith("Windows"):
        os.system('cls')
        import parcel

     if platform.system().startswith("Linux"):
        os.system('python3 parcel.py')
     elif platform.system().startswith("Windows"):
        import parcel


# OPTION 3


if option == 3:
     print(f"{Fore.RED}[", end=''), print(f'{colored.fg(172)}+', end=''), print(f"{Fore.RED}]", end=''), print(f'{colored.fg(172)} Please Wait ')
    
     time.sleep(3)
     if platform.system().startswith("Linux"):
        os.system('clear')
     elif platform.system().startswith("Windows"):
        os.system('cls')


# GITHUB


if option == 9:
        print(f"{Fore.CYAN}[", end=''), print(f'{colored.fg(243)}+', end=''), print(f"{Fore.CYAN}]", end=''), print(f'{colored.fg(243)} Redirection in progres... ')
        time.sleep(1)
        webbrowser.open('https://github.com/tayko9222/screamtool/')


# OPTION 4


if option == 4:
    if platform.system().startswith("Linux"):
        os.system('clear')
    elif platform.system().startswith("Windows"):
        os.system('cls')

    time.sleep(1.25)

    if platform.system().startswith("Linux"):
        os.system('python3 parcel2.py')
    elif platform.system().startswith("Windows"):
        import parcel2


# EXIT

if option == 0:

    if platform.system().startswith("Linux"):
        os.system('clear')
    elif platform.system().startswith("Windows"):
        os.system('cls')

    print(f"{Fore.RED}[", end=''), print(f'{colored.fg(172)}+', end=''), print(f"{Fore.RED}]", end=''), print(f'{colored.fg(172)} Leaving In Progres... ')
    
    time.sleep(1.25)
    if platform.system().startswith("Linux"):
        os.system('clear')
    elif platform.system().startswith("Windows"):
        os.system('cls')
    exit()















                       
