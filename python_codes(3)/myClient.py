import socket

# Create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = 'localhost' #socket.gethostname()

# Reserve a port for your service
port = 12345

# Connect to the server
clientsocket.connect((host, port))

# Receive data from the server
data = clientsocket.recv(1024)

# Print the received data
print(f'Received data: {data.decode("utf-8")}')

# Send a message to the server
message = 'Hello, server!'
clientsocket.send(message.encode('utf-8'))

# Close the connection
clientsocket.close()
