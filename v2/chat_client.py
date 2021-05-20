import sys, time, socket, threading

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

banner_slowprint(bcolors.HEADER+banner+bcolors.ENDC)
slowprint(bcolors.WARNING+"[CONNECTING] Connecting to server..."+bcolors.ENDC)
slowprint(bcolors.GREEN+"[CONNECTED] Connected to server..."+bcolors.ENDC)
nickname = input(bcolors.GREEN+"[+] Enter your nickname: "+bcolors.ENDC)

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
            slowprint(bcolor.FAIL+"[ERROR] An error occured!"+bcolors.ENDC)
            client.close()
            break
def write():
    while True:                                                
        message = '[{}] >> {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)              
receive_thread.start()
write_thread = threading.Thread(target=write)                   
write_thread.start()


