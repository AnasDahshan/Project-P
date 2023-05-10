import socket

# Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = 'localhost' #socket.gethostname()

# Reserve a port for your service
port = 12345

# Bind the socket to a specific address and port
serversocket.bind((host, port))

# Listen for incoming connections
serversocket.listen(1)

# Wait for a connection
print('Waiting for a client to connect...')
clientsocket, addr = serversocket.accept()

# Connection established
print(f'Connection established with {addr}')

# Send a welcome message to the client
message = 'Welcome to the server!'
clientsocket.send(message.encode('utf-8'))
# Note that message.encode('utf-8') is converting the Python string 'message'
# into a sequence of bytes that can be sent over the network using the
# UTF-8 encoding.

# Receive data from the client
data = clientsocket.recv(1024)

# Print the received data
print(f'Received data: {data.decode("utf-8")}')
# we need to decode the received data using decode("utf-8") to convert it back into a
# Python string that we can work with.

# Close the connection
clientsocket.close()
