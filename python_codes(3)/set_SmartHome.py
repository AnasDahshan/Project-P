# Suppose you have a smart home with various smart devices,
# such as smart lights, smart locks, and smart thermostats.
# You want to keep track of the different types of devices
# in your home, and you want to be able to quickly check if a
# specific type of device is in your home.
# You can use sets to achieve this.

# create a set of device types in your smart home
device_types = {"smart lights", "smart locks", "smart thermostats"}

# add a new device type
device_types.add("smart speakers")

# remove a device type
device_types.remove("smart thermostats")

# check if a specific device type is in your smart home
if "smart lights" in device_types:
    print("You have smart lights in your home!")

# find the intersection of the device types with a set of security devices
security_devices = {"smart locks", "security cameras"}
secure_devices = device_types.intersection(security_devices)

# print the results
print("All device types:", device_types)
print("Secure device types:", secure_devices)
