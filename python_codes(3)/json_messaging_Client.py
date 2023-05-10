import socket
import json

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        message = input('Enter message to send: ')
        data = {'message': message}
        sock.sendall(json.dumps(data).encode())
        response = sock.recv(1024)
        received_data = json.loads(response.decode())
        print('Received:', received_data['message'])
