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
print(f"{Fore.CYAN}[{Fore.RED}+{Fore.CYAN}]{Fore.CYAN} Please wait ")
time.sleep(3)
os.system('cls')

print(Fore.CYAN + "   ___  _  _   __   __  __        ____  ____   __   _  _  _  _  ____  ____ ")
print(Colors.red, " / __)( \/ ) / _\ (  )(  )      / ___)(  _ \ / _\ ( \/ )( \/ )(  __)(  _ /")
print(Colors.orange, "( (_ \/ \/ \/    \ )( / (_/\    \___ \ ) __//    \/ \/ \/ \/ \ ) _)  )   /")
print(Fore.BLUE + "  \___/\_)(_/\_/\_/(__)\____/    (____/(__)  \_/\_/\_)(_/\_)(_/(____)(__\_)")
print(f"{Fore.YELLOW}                                                        [{Fore.BLUE}v.12345{Fore.YELLOW}] ")
print("")
print("")
print("")
print("")
print(f"{Fore.RED}[",end=''), print(f'{Fore.BLUE}!', end=''), print(f"{Fore.RED}] ", end='') , print(f'{Fore.BLUE}Please press ENTER ', end=''), print(f"{Fore.RED}")
input(" > ")



os.system('cls')

print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}?', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Email of the victim ')
victime = input(" > ")

print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}?', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Please re enter the victim email ')
verif = input(" > ")

if victime==verif:
    print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}?', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Write a message', end=''), print(f'{colored.fg(231)} ( Recommanded is "test" )', end=''), print(f'{colored.fg(84)}') 
    message = input(" > ")

else:
    print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}!', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(8)}The email doesnt match please try again ')
    time.sleep(1.5)
    os.system('cls')
    exit()


print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}?', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Your gmail ')
mail = input(" > ")

print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}?', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(84)}Your Gmail password ')
pswd = input(" > ")

if smtplib.SMTPAuthenticationError:
    print(f"{Fore.RED}[{Fore.CYAN}+{Fore.RED}]{Fore.WHITE} How many mail you want to send ? ", end=''), print(f'{colored.fg(231)} ( Max is 100 )', end=''), print(f'{Fore.RED}')
    time.sleep(2.5)
    os.system('cls')
    exit()


with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    os.system('cls')
    print((f"{Fore.CYAN}[{Fore.RED}!{Fore.CYAN}]{Fore.RED} Email used is noreply6481738240@gmail.com )"))
    smtpserver.login(mail, pswd)
    time.sleep(2.5)

    os.system('cls')
    print(f"{Fore.CYAN}[{Fore.RED}+{Fore.CYAN}]{Fore.CYAN} How many mail you want to send ? ", end=''), print(f'{colored.fg(231)} ( Max is 100 )', end=''), print(f'{Fore.RED}')
    for i in range(int(input(" > "))):
        smtpserver.sendmail(victime, verif, message)
        print(f"{Fore.CYAN}[{Fore.RED}+{Fore.CYAN}]{Fore.CYAN} Number of email who was sent : ", f"{Fore.RED}",i)

