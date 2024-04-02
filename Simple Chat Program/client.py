from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
host_ip = '127.0.0.1'
port = 8000
client_socket.connect((host_ip, port))

while True:
    client_msg = input('Client: ') + '\r\n'
    client_socket.sendall(client_msg.encode('utf-8'))

    server_msg = ''
    while True:
        part_of_msg = client_socket.recv(1024).decode('utf-8')
        server_msg += part_of_msg

        if '\r\n' in server_msg:
            break

    server_msg = server_msg.strip()

    if server_msg == 'quit':
        break
    print(f'Server: {server_msg}')

client_socket.close()
