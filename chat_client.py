import socket, threading

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
print(banner)
nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     
client.connect(('127.0.0.1', 5555))                            

def receive():
    while True:                                                
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:                                                
            print("An error occured!")
            client.close()
            break
def write():
    while True:                                                
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)              
receive_thread.start()
write_thread = threading.Thread(target=write)                   
write_thread.start()
