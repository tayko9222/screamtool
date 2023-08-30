import time
import os
import pystyle
import colorama
import colored
import smtplib
import requests
import platform
import sys
from tqdm import tqdm
from colored import *
from pystyle import Colors, Colorate
from colorama import *



os.system('cls')
print(f"{Fore.RED}[", end=''), print(f'{colored.fg(172)}+', end=''), print(f"{Fore.RED}]", end=''), print(f'{colored.fg(172)} Please Wait ')
time.sleep(3)
os.system('cls')

if platform.system() == "Windows":
            os.system('cls')
else:
            os.system('clear')

time.sleep(1)
print(f"{Fore.CYAN}[{Fore.BLACK}!{Fore.CYAN}] ", end='') , print(f'{colored.fg(2)} Enter the target number ')
smsnumb = input(" > ")
print(f"{Fore.CYAN}[{Fore.BLACK}!{Fore.CYAN}] ", end='') , print(f'{colored.fg(2)} Enter the message who going to send ')
message = input(" > ")

resp = requests.post('https://textbelt.com/text', {
            'phone': f'{smsnumb}',
            'message': f'{message}',
            'key': 'textbelt',
        })

print(resp.json())
time.sleep(5)

if platform.system() == "Windows":
            os.system('cls')
else:
            os.system('clear')