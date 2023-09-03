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

print(Fore.CYAN + "  ____   ___  ____  ____   __   _  _      ____  _  _  ____ ")
print(Colors.red, "/ ___) / __)(  _ \(  __) / _\ ( \/ )    (_  _)( \/ )(  _ /")
print(Colors.orange, "\___ \( (__  )   / ) _) /    \/ \/ \      )(   )  (  )   /")
print(Fore.BLUE + " (____/ \___)(__\_)(____)\_/\_/\_)(_/     (__) (_/\_)(__\_)")
print(f"{Fore.YELLOW}                                                  [{Fore.BLUE}v.10000{Fore.YELLOW}] ")
print(f"{Fore.LIGHTBLUE_EX}                                                [{Fore.RED}By {Fore.CYAN}Newark{Fore.LIGHTBLUE_EX}] ")
print("")
print("")
print("")
print("")

print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}01', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Dox with username ')
print("")
print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}02', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Dox with email ')
print("")
print("")
print("")
print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}0', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Exit ', end=''), print("                ", end=''), print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}9', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Github ', end=''),print("                ", end=''), print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}h', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Help ')
print("      ")
print("      ")
print("      ")

print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}?', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Please choose an option ')

opt = int(input(" > "))

if opt == 1:

    if platform.system().startswith("Linux"):
        os.system('clear')
    elif platform.system().startswith("Windows"):
        os.system('cls')

    if platform.system().startswith("Linux"):
        os.system('python3 doxu.py')
    elif platform.system().startswith("Windows"):
        import doxu

if opt == 2:
    if platform.system().startswith("Linux"):
        os.system('python3 doxm.py')
    elif platform.system().startswith("Windows"):
        import doxm
