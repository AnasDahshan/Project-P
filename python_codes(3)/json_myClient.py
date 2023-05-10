import socket
import json
import random
import time

# Create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service
port = 12345

# Connect to the server
clientsocket.connect((host, port))

# Receive the welcome message from the server
data = clientsocket.recv(1024)
print(data.decode('utf-8'))

# Generate random sensor data
sensor_data = {
    'id': 'sensor001',
    'temperature': round(random.uniform(20.0, 30.0), 2),
    'humidity': round(random.uniform(30.0, 50.0), 2)
}

# Convert the sensor data to JSON format
data_str = json.dumps(sensor_data)

# Send the sensor data to the server
clientsocket.send(data_str.encode('utf-8'))

# Close the connection
clientsocket.close()
