# Consider an IoT application that involves monitoring the temperature of a
# chemical reaction and signaling an alert when the temperature goes
# beyond a certain threshold:

# Import necessary libraries
import time
import random

# Threshold temperature (in Celsius)
threshold_temperature = 70

# Start monitoring
while True:
    # Get current temperature reading (Simulate temperature readings)
    temperature = random.randint(0, 100)
    
    # Check if temperature is above threshold
    if temperature > threshold_temperature:
        print("Alert: Temperature is above threshold!")
    else:
        print("Safe!")
    
    # Wait for 2 seconds before taking the next reading
    time.sleep(2)
