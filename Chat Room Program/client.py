from threading import *
from socket import *

client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect(('127.0.0.1',8000))
nickname = input('nickname>>> ')

def client_receive():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')

            if message == 'nickname?':
                client_socket.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print('ERROR!')
            client_socket.close()
            break


def client_send():
    while True :
        message = f'{nickname} : {input("")}'
        client_socket.send(message.encode('utf-8'))

receive_thread = Thread(target=client_receive)
receive_thread.start()

send_thread = Thread(target=client_send)
send_thread.start()



