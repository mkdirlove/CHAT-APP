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
 _____ _____ _____ _____ _____ _____ 
|   __|   __| __  |  |  |   __| __  |
|__   |   __|    -|  |  |   __|    -|
|_____|_____|__|__|\___/|_____|__|__|

[+] Welcome to our simple chatroom [+]
"""

host = '127.0.0.1'                                                      
port = 12345                                                     

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              
server.bind((host, port))                                               
server.listen()

clients = []
nicknames = []


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
		
def broadcast(message):                                                 
    for client in clients:
        client.send(message)

def handle(client):                                         
    while True:
        try:                                                            
            message = client.recv(1024)
            broadcast(message)
        except:                                                         
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast("{} left in the chatroom!\n".format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():                                                          
    while True:
        try:
            client, address = server.accept()
            slowprint(f"{bcolors.GREEN}[CONNECTED] Connected with {str(address)}")       
            client.send('NICKNAME'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            nicknames.append(nickname)
            clients.append(client)
            broadcast("[CLIENT] {} joined in the chatroom!".format(nickname).encode('ascii'))
            #client.send('[!] Connected to the server...\n'.encode('ascii'))
            #client.send('\n[+] You can now start chatting...'.encode('ascii'))
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
        except KeyboardInterrupt:
            slowprint(f"{bcolors.FAIL}[ERROR] error he was forced{bcolors.ENDC}")
            exit(1)

if __name__ == '__main__':
    clear_pan()
    banner_slowprint(bcolors.HEADER+banner+bcolors.ENDC)
    slowprint(f"{bcolors.WARNING}[STARTING] Server is starting...{bcolors.ENDC}")
    slowprint(f"{bcolors.GREEN}[STARTED] Server is up and running...{bcolors.ENDC}")
    slowprint(f"{bcolors.BLUE}[WAITING] Waiting for clients to connect...{bcolors.ENDC}")
    receive()
