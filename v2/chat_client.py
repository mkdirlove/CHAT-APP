#!/usr/bin/python3

from os import system
import sys, time, socket, threading, platform

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
banner = """                     
       _____ _____ _____ _____           
      |     |  |  |  _  |_   _|          
      |   --|     |     | | |            
      |_____|__|__|__|__| |_|                                         
 _____ __    _____ _____ _____ _____ 
|     |  |  |     |   __|   | |_   _|
|   --|  |__|-   -|   __| | | | | |  
|_____|_____|_____|_____|_|___| |_|  

      [+] Welcome clients [+]
"""

def clear_pan():
    if platform.system() == "Linux":
        system("clear")
    else:
        exit(1)


def banner_slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(.01/10)


def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1/10)


try:
    clear_pan()
    banner_slowprint(bcolors.HEADER+banner+bcolors.ENDC)
    slowprint(f"{bcolors.WARNING}[CONNECTING] Connecting to server...{bcolors.ENDC}")
    slowprint(f"{bcolors.GREEN}[CONNECTED] Connected to server...{bcolors.ENDC}")
    nickname = input(f"{bcolors.GREEN}[+] Enter your nickname: {bcolors.ENDC}")
except KeyboardInterrupt as e:
    slowprint(f"{bcolors.FAIL}[ERROR] error he was forced")
    print(e)
    exit(1)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '127.0.0.1'
port = 12345     
client.connect((server, port))                            


def receive():
    while True:                                                
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:                                                
            slowprint(f"{bcolors.FAIL}[ERROR] An error occured!{bcolors.ENDC}")
            client.close()
            break


def write():
    while True:  
        try:                                              
            message = f'[{nickname}] >> {input("")}'
            client.send(message.encode('ascii'))
        except KeyboardInterrupt:
            slowprint(f"{bcolors.FAIL}[ERROR] error he was forced") 
            exit(1)


if __name__ == '__main__':
    receive_thread = threading.Thread(target=receive)              
    receive_thread.start()
    write_thread = threading.Thread(target=write)                   
    write_thread.start()


