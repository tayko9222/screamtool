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

print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}?', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Email of the victim ')
victime = input(" > ")

print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}?', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Please re enter the victim email ')
sender = input(" > ")

if victime==sender:
    print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}?', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Write a message ')
    message = input(" > ")

else:
    print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}!', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(8)}The email doesnt match please try again ')
    time.sleep(1.5)
    os.system('cls')
    exit()



with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(input("The sender email > "), input("Your App Passwords > "))
    for i in range(2):
        smtpserver.sendmail(victime, sender, message)
        print(f"{Fore.CYAN}[{Fore.RED}+{Fore.CYAN}] ", end='') , print(f'{colored.fg(172)} Number of email who was sent : ', i)