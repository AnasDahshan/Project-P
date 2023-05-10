# create a dictionary for a smart car
smart_car = {
    'make': 'Tesla',
    'model': 'Model 3',
    'year': 2022,
    'battery_capacity': 75,  # kWh
    'max_speed': 233,  # km/h
    'color': 'red',
    'price': 45000  # USD
}

# make a copy of the dictionary
smart_car_copy = smart_car.copy()

# update the copy with some new values
smart_car_copy.update({
    'color': 'blue',
    'price': 50000
})

# use the .items() function to loop through the original dictionary and print its key-value pairs
for key, value in smart_car.items():
    print(f"{key}: {value}")

# print a separator
print('-' * 20)

# use the .items() function to loop through the copied dictionary and print its key-value pairs
for key, value in smart_car_copy.items():
    print(f"{key}: {value}")
