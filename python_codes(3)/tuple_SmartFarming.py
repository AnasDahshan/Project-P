# Let's say you're building a smart farming application that includes
# a variety of sensors, such as soil moisture sensors, temperature sensors,
# and light sensors. Each sensor generates a set of data that includes the
# sensor's ID, the type of data (e.g. soil moisture, temperature, or light),
# and the current value of the data.
# You could represent this data as a tuple for each sensor, with the sensor's
# ID as the first element, the data type as the second element, and the current
# value as the third element.

# define a tuple for a soil moisture sensor
soil_moisture_sensor = ('soil001', 'soil moisture', 0.6)

# define a tuple for a temperature sensor
temp_sensor = ('temp001', 'temperature', 25.6)

# define a tuple for a light sensor
light_sensor = ('light001', 'light', 60)

# print the tuples
print(soil_moisture_sensor)
print(temp_sensor)
print(light_sensor)

# You could store these tuples in a list or dictionary to keep track of
# all the sensors in your system

# create a list of sensor tuples
sensors = [soil_moisture_sensor, temp_sensor, light_sensor]

# loop through the sensor tuples and print the data
for sensor in sensors:
    print(f"{sensor[0]}: {sensor[2]} {sensor[1]}")

