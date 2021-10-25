#!/usr/bin/python3

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

server_socket.bind((host, port))
server_socket.listen(3)

while True:
    client_socket, address = server_socket.accept()
    print('received connection from: {}'.format(address))
    message = 'hello, thank you for connecting on this server ʕ•́ᴥ•̀ʔっ' + '\r\n'
    client_socket.send(message)

    client_socket.close()
