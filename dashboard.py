import tkinter as tk
import threading
import webbrowser

from vehicle_sim import Vehicle
from intent_model import predict_intent
from rag_engine import answer_question
from voice import speak, listen
from obd_sim import read_fault
from memory_nav import save_place

# -----------------------------
# Initialize Vehicle
# -----------------------------
car = Vehicle()

# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("AI Vehicle CoPilot Dashboard")
root.geometry("400x350")

speed_label = tk.Label(root, text="Speed: --", font=("Arial", 16))
fuel_label = tk.Label(root, text="Fuel: --", font=("Arial", 16))
temp_label = tk.Label(root, text="Temperature: --", font=("Arial", 16))
command_label = tk.Label(root, text="Command: ", font=("Arial", 12))
response_label = tk.Label(root, text="Response: ", font=("Arial", 12), wraplength=350)

speed_label.pack(pady=10)
fuel_label.pack(pady=10)
temp_label.pack(pady=10)
command_label.pack(pady=10)
response_label.pack(pady=10)

# -----------------------------
# AI LOOP
# -----------------------------
def ai_loop():
    speak("AI Vehicle CoPilot Started")

    while True:

        car.update()
        data = car.get_data()

        speed_label.config(text=f"Speed: {data['speed']}")
        fuel_label.config(text=f"Fuel: {data['fuel']}")
        temp_label.config(text=f"Temperature: {data['engine_temp']}")

        command = listen()
        if command == "":
            continue

        command_label.config(text=f"Command: {command}")
        intent = predict_intent(command)

        if "stop" in command or "emergency" in command:
            reply = "Emergency mode activated"

        elif intent == "speed":
            reply = f"Speed is {data['speed']}"

        elif intent == "fuel":
            reply = f"Fuel level is {data['fuel']} percent"

        elif intent == "temp":
            reply = f"Engine temperature is {data['engine_temp']}"

        elif intent == "navigate":
            destination = command.replace("navigate to", "").replace("go to", "").strip()
            url = f"https://www.google.com/maps/search/{destination}"
            webbrowser.open(url)
            save_place(destination)
            reply = f"Opening Google Maps for {destination}"

        elif intent == "question":
            reply = answer_question(command)

        elif intent == "diagnostic":
            code, meaning = read_fault()
            reply = f"Fault code {code}. {meaning}"

        else:
            reply = "Command not recognized"

        print("Assistant:", reply)
        response_label.config(text=f"Response: {reply}")
        speak(reply)

# -----------------------------
threading.Thread(target=ai_loop, daemon=True).start()
root.mainloop()
