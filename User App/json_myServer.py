import socket
import json

# Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

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

# Receive data from the client
data = clientsocket.recv(1024)

# Convert the received data from bytes to string
data_str = data.decode('utf-8')

# Load the data from JSON format
sensor_data = json.loads(data_str)

# Process the sensor data
sensor_id = sensor_data['id']
temperature = sensor_data['temperature']
humidity = sensor_data['humidity']

print(f'Received sensor data from {sensor_id}:')
print(f'Temperature: {temperature}°C')
print(f'Humidity: {humidity}%')

# Close the connection
clientsocket.close()
