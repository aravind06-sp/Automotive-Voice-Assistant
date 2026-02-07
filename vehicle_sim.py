# vehicle_sim.py
import random
import time

class Vehicle:
    def __init__(self):
        self.speed = 0
        self.fuel = 100
        self.engine_temp = 75
        self.rpm = 900
        self.battery_voltage = 12.6

    def update(self):
        # Generate realistic random values
        self.speed = random.randint(0, 120)
        self.fuel = random.randint(10, 100)
        self.engine_temp = random.randint(70, 110)
        self.rpm = random.randint(800, 4000)
        self.battery_voltage = round(random.uniform(11.8, 14.4), 2)

    def get_data(self):
        # Return latest values
        return {
            "speed": self.speed,
            "fuel": self.fuel,
            "engine_temp": self.engine_temp,
            "rpm": self.rpm,
            "battery_voltage": self.battery_voltage
        }


# Standalone test
if __name__ == "__main__":
    car = Vehicle()
    while True:
        car.update()
        print(car.get_data())
        time.sleep(1)
