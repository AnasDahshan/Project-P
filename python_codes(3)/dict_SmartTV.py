# create a dictionary for a smart TV
smart_tv = {
    'brand': 'Samsung',
    'model': 'QLED Q90T',
    'year': 2020,
    'screen_size': 55,  # inches
    'resolution': '4K',
    'price': 1499,  # USD
    'apps': ['Netflix', 'YouTube', 'Amazon Prime Video']
}

# add a new key-value pair to the dictionary
smart_tv['color'] = 'black'

# update an existing key-value pair in the dictionary
smart_tv.update({'year': 2021})

# use the .items() function to loop through the dictionary and print its key-value pairs
for key, value in smart_tv.items():
    print(f"{key}: {value}")

# remove a key-value pair from the dictionary
del smart_tv['price']
print('-'*20)
# use the .items() function to loop through the updated dictionary and print its key-value pairs
for key, value in smart_tv.items():
    print(f"{key}: {value}")
