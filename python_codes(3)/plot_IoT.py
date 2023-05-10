import random
import time
import matplotlib.pyplot as plt

# Define a function to read sensor data
def read_sensor():
    # Generate random sensor data between 0 and 100
    return random.randint(0, 100)

# Create a list to store the sensor data
data = []

# Collect sensor data for 10 seconds
for i in range(10):
    # Read the sensor data
    sensor_data = read_sensor()
    # Append the sensor data to the list
    data.append(sensor_data)
    # Wait for 1 second before collecting the next sensor data
    time.sleep(1)

# Create a plot to visualize the sensor data
plt.plot(data)
plt.xlabel('Time (s)')
plt.ylabel('Sensor Data')
plt.show()
