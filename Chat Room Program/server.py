#Server-Side

from threading import *
from socket import *

server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('127.0.0.1',8000))
server_socket.listen(5)
clients = []
nicknames=[]

def broadcast(message,client_session):
    for client in clients :
        if client != client_session:
            client.send(message.encode('utf-8'))


def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            broadcast(message,client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            message = f'{nickname} has left the chat room'
            broadcast(message,client)
            nicknames.remove(nickname)
            break

def receive():

    while True :
        print('server is running and listening...')
        client , address = server_socket.accept()
        client.send('nickname?'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        clients.append(client)
        nicknames.append(nickname)
        print(f'connection is established with {address}')
        print(f'The alias of this client is {nickname}')
        message = f'{nickname} is connected to chat room'
        broadcast(message,client)
        client.send('you are now connected'.encode('utf-8'))
        thread = Thread(target=handle_client,args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()






            


