from vehicle_sim import Vehicle
from voice import speak

car = Vehicle()
print("AI Vehicle CoPilot Started")
speak("AI Vehicle CoPilot Started")

while True:
    car.update()
    data = car.get_data()

    message = f"Speed {data['speed']} Fuel {data['fuel']} Temperature {data['engine_temp']}"
    print(message)
    speak(message)

    input("Press Enter to update...")
