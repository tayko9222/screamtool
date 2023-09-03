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



if platform.system().startswith("Linux"):
    os.system('clear')
elif platform.system().startswith("Windows"):
    os.system('cls')

print(f"{Fore.CYAN}[{Fore.RED}+{Fore.CYAN}]{Fore.RED} Please wait ", end=''), print(f"{Fore.CYAN}")

time.sleep(3)

if platform.system().startswith("Linux"):
    os.system('clear')
elif platform.system().startswith("Windows"):
    os.system('cls')


print(Fore.CYAN + "  ____  _____  _  _ ")
print(Colors.red, "(  _ \(  _  )( \/ )")
print(Colors.orange, " )(_) ))(_)(  )  ( ")
print(Fore.BLUE + " (____/(_____)(_/\_)")
print(f"{Fore.YELLOW}           [{Fore.BLUE}v.12345{Fore.YELLOW}] ")
print("")
print("")
print("")
print("")
print(f"{Fore.CYAN}[",end=''), print(f'{Fore.RED}!', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{Fore.RED}Please press ENTER ', end=''), print(f"{Fore.CYAN}")
input(" > ")



if platform.system().startswith("Linux"):
    os.system('clear')
elif platform.system().startswith("Windows"):
    os.system('cls')



print(f"{Fore.CYAN}[",end=''), print(f'{Fore.RED}!', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{Fore.RED}Enter A Username ', end=''), print(f"{Fore.CYAN}")
usname = input(" > ")

print(f"{Fore.CYAN}[",end=''), print(f'{Fore.RED}!', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{Fore.RED}Please re enter the username ', end=''), print(f"{Fore.CYAN}")
uverif = input(" > ")

if platform.system().startswith("Linux"):
        os.system('clear')
elif platform.system().startswith("Windows"):
    os.system('cls')

if usname==uverif:
    print(f"{Fore.CYAN}[",end=''), print(f'{Fore.RED}!', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{Fore.RED}Did you want a custom site list ?', end=''), print(f'{Fore.WHITE} ( y/n )', end=''), print(f"{Fore.CYAN}") 
    message = input(" > ")

else:
    print(f"{Fore.CYAN}[",end=''), print(f'{colored.fg(231)}!', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{colored.fg(8)}The email doesnt match please try again ')
    time.sleep(1.5)
    if platform.system().startswith("Linux"):
        os.system('clear')
    elif platform.system().startswith("Windows"):
        os.system('cls')
    exit()

if message.startswith('n'):
    print(f"{Fore.CYAN}[",end=''), print(f'{Fore.RED}!', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{Fore.RED}Ok, if you want change please restart', end=''), print(f'{Fore.WHITE} ( You are using default site list )', end=''), print(f"{Fore.CYAN}")
    time.sleep(3)
    if platform.system().startswith("Linux"):
        os.system('clear')
    elif platform.system().startswith("Windows"):
        os.system('cls')

    print(f"{Fore.RED}[{Fore.CYAN} 1 {Fore.RED}]", end=''), print(f"{Fore.RED} https://{Fore.CYAN}instagram{Fore.RED}.com/@{Fore.CYAN}" + usname)
    print(f"{Fore.RED}[{Fore.CYAN} 2 {Fore.RED}]", end=''), print(f"{Fore.RED} https://{Fore.CYAN}tiktok{Fore.RED}.com/@{Fore.CYAN}" + usname)
    print(f"{Fore.RED}[{Fore.CYAN} 3 {Fore.RED}]", end=''), print(f"{Fore.RED} https://{Fore.CYAN}snapchat{Fore.RED}.com/add/{Fore.CYAN}" + usname)
    print(f"{Fore.RED}[{Fore.CYAN} 4 {Fore.RED}]", end=''), print(f"{Fore.RED} https://{Fore.CYAN}twitter{Fore.RED}.com/{Fore.CYAN}" + usname)
    print(f"{Fore.RED}[{Fore.CYAN} 5 {Fore.RED}]", end=''), print(f"{Fore.RED} https://{Fore.CYAN}facebook{Fore.RED}.com/{Fore.CYAN}" + usname)    
    print(f"{Fore.RED}[{Fore.CYAN} 6 {Fore.RED}]", end=''), print(f"{Fore.RED} https://{Fore.CYAN}t{Fore.RED}/{Fore.CYAN}.me/" + usname)
    print(f"{Fore.RED}[{Fore.CYAN} 7 {Fore.RED}]", end=''), print(f"{Fore.RED} https://{Fore.CYAN}facebook{Fore.RED}.com/@{Fore.CYAN}" + usname)
    print("")
    print(f"{Fore.RED}[",end=''), print(f'{Fore.CYAN}!', end=''), print(f"{Fore.RED}] ", end='') , print(f'{Fore.RED}If you want open a link write his number ', end=''), print(f"{Fore.CYAN}")
    print("", end=''), print(f"{Fore.CYAN}")
    sqst = input(" > ")



if sqst==1:
    time.sleep(0.5)
    webbrowser.open('https://instagram.com/@'+usname)
    print(f"{Fore.CYAN}[", end=''), print(f'{colored.fg(243)}+', end=''), print(f"{Fore.CYAN}]", end=''), print(f'{colored.fg(243)} Redirection in progres... ', end=''), print(f"{Fore.WHITE}")
    time.sleep(1)
    sqst = input(" > ")

elif sqst==2:
    time.sleep(0.5)
    webbrowser.open('https://tiktok.com/@'+usname)
    print(f"{Fore.CYAN}[", end=''), print(f'{colored.fg(243)}+', end=''), print(f"{Fore.CYAN}]", end=''), print(f'{colored.fg(243)} Redirection in progres... ', end=''), print(f"{Fore.WHITE}")
    time.sleep(1)
    sqst = input(" > ")   


elif message.startswith('y'):
    print(f"{Fore.CYAN}[",end=''), print(f'{Fore.RED}!', end=''), print(f"{Fore.CYAN}] ", end='') , print(f'{Fore.RED}Please enter how many site did you want ')
    cstmstamnt=input(" > ")






    




        
