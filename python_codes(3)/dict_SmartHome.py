# Define a dictionary to store smart home device settings
smart_home = { "thermostat": {"temperature": 72,"mode": "auto","fan": "on"},
                   "lights": {"living_room": {"brightness": 50,"color": "white"}, "bedroom": { "brightness": 75, "color": "yellow"}},
                     "lock": {"status": "unlocked", "code": 1234}}

# Access and update settings for the thermostat
print(smart_home["thermostat"]["temperature"]) # Output: 72
smart_home["thermostat"]["temperature"] = 70
print(smart_home["thermostat"]["temperature"]) # Output: 70

# Access and update settings for the living room lights
print(smart_home["lights"]["living_room"]["brightness"]) # Output: 50
smart_home["lights"]["living_room"]["brightness"] = 100
print(smart_home["lights"]["living_room"]["brightness"]) # Output: 100

# Lock the front door
smart_home["lock"]["status"] = "locked"
print(smart_home["lock"]["status"]) # Output: locked

