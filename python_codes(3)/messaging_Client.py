import socket

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        message = input('Enter message to send: ')
        sock.sendall(message.encode())
        data = sock.recv(1024)
        print('Received:', data.decode())
