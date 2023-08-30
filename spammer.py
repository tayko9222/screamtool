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

print(f"{Fore.CYAN}[{Fore.BLACK}?{Fore.CYAN}] ", end='') , print(f'{colored.fg(2)} Email of the victim ')
victime = input(" > ")

print(f"{Fore.CYAN}[{Fore.BLACK}?{Fore.CYAN}] ", end='') , print(f'{colored.fg(2)} Please re enter the victim email ')
sender = input(" > ")

if victime==sender:
    print(f"{Fore.CYAN}[{Fore.BLACK}?{Fore.CYAN}] ", end='') , print(f'{colored.fg(2)} Write a message ')
    message = input(" > ")

else:
    print(f"{Fore.CYAN}[{Fore.BLACK}!{Fore.CYAN}] ", end='') , print(f'{colored.fg(1)} Emails doesnt match please try again ')
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