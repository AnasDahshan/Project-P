# Example of using a list data structure for an IoT application

# Initialize a list of sensor values
sensor_values = [20.3, 21.2, 19.8, 22.1, 20.9]

# Function to calculate the average of the sensor values
total = 0
for value in sensor_values:
    total += value
    average = total / len(sensor_values)
    
# Print the average of the sensor values
print("Average sensor value:", sensor_values)

# Add a new sensor value to the list
new_value = 23.5
sensor_values.append(new_value)

# Print the updated list of sensor values
print("Updated sensor values:", sensor_values)
