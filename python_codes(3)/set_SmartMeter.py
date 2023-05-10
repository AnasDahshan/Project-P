# Suppose you have a smart metering system that monitors energy usage
# in a building. You want to keep track of the different types of
# energy meters in the building, and you want to be able to quickly
# check if a specific type of meter is in use. You can use sets to
# achieve this.

# create a set of energy meter types in the building
meter_types = {"electricity", "gas", "water"}

# add a new meter type
meter_types.add("solar")

# remove a meter type
meter_types.remove("gas")

# check if a specific meter type is in use
if "electricity" in meter_types:
    print("Electricity meter is in use.")

# find the intersection of the meter types with a set of renewable energy sources
renewable_sources = {"solar", "wind"}
renewable_meters = meter_types.intersection(renewable_sources)

# print the results
print("All meter types:", meter_types)
print("Renewable meter types:", renewable_meters)
