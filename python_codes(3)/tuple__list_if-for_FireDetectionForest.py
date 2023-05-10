# define a list of sensor readings
sensor_readings = [
    ('temp001', 'temperature', 25.6),
    ('humid001', 'humidity', 50),
    ('smoke001', 'smoke', 0),
    ('fire001', 'fire', 0)
]

# define a dictionary of thresholds for each sensor type
thresholds = {
    'temperature': 30,
    'humidity': 70,
    'smoke': 100,
    'fire': 1
}

# loop through the sensor readings and check for fires
for reading in sensor_readings:
    sensor_id, sensor_type, sensor_value = reading
    
    # check if the sensor value exceeds the threshold for its type
    if sensor_value > thresholds[sensor_type]:
        print(f"Fire detected by sensor {sensor_id} ({sensor_type}: {sensor_value})")
        # send a notification or take some other action to respond to the fire
    else:
        print(f"No fire detected by sensor {sensor_id} ({sensor_type}: {sensor_value})")
