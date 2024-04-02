from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
host_ip = '127.0.0.1'
port = 8000
server_socket.bind((host_ip, port))
server_socket.listen(5)

client_session, client_addr = server_socket.accept()
print(f'Connection from {client_addr[0]}')

while True:
    client_msg = ''
    while True:
        part_of_msg = client_session.recv(1024).decode('utf-8')
        client_msg += part_of_msg

        if '\r\n' in client_msg:
            break

    client_msg = client_msg.strip()

    if client_msg == 'quit':
        break
    else:
        print(f'Client: {client_msg}')
    
    server_msg = input('Server: ') + '\r\n'
    client_session.sendall(server_msg.encode('utf-8'))

client_session.close()
