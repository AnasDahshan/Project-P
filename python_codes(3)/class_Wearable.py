class WearableDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.temperature = 0
        self.heart_rate = 0
        self.steps = 0

    def set_temperature(self, temperature):
        self.temperature = temperature

    def set_heart_rate(self, heart_rate):
        self.heart_rate = heart_rate

    def set_steps(self, steps):
        self.steps = steps

    def get_device_id(self):
        return self.device_id

    def get_temperature(self):
        return self.temperature

    def get_heart_rate(self):
        return self.heart_rate

    def get_steps(self):
        return self.steps

smartwatch = WearableDevice("12345")
smartwatch.set_temperature(37)
smartwatch.set_heart_rate(85)
smartwatch.set_steps(5000)

print(smartwatch.get_device_id())  # prints "12345"
print(smartwatch.get_temperature())  # prints 37
print(smartwatch.get_heart_rate())  # prints 85
print(smartwatch.get_steps())  # prints 5000
