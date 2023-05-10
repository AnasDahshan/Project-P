import socket
import json

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            received_data = json.loads(data.decode())
            print('Received:', received_data)
            response_data = {'message': 'ACK'}
            conn.sendall(json.dumps(response_data).encode())


