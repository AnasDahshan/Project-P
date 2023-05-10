import time
import random

def read_sensor_data(sensor_id, sensor_type):
    # Simulate reading sensor data from a sensor with the given ID and type
    if sensor_type == "light":
        light_intensity = random.uniform(0, 100)
        data = f"{int(time.time())},{sensor_id},{light_intensity:.2f}"
    elif sensor_type == "motion":
        motion_detected = random.choice([True, False])
        data = f"{int(time.time())},{sensor_id},{int(motion_detected)}"
    elif sensor_type == "sound":
        decibel_level = random.uniform(0, 120)
        data = f"{int(time.time())},{sensor_id},{decibel_level:.2f}"
    else:
        data = f"{int(time.time())},{sensor_id},0"

    return data

# Example usage: read sensor data from a light sensor with ID 456 and
# print the result
sensor_type = input("Enter the sensor type ('light','motion', or 'sound'): ")
sensor_data = read_sensor_data(456, "sound")
print(sensor_data)
