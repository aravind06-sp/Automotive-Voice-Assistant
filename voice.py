import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init(driverName='sapi5')

engine.setProperty('rate', 165)

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.pause_threshold = 0.8

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone(device_index=1) as source:  # keep your mic index
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

        command = recognizer.recognize_google(audio, language="en-IN")
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        return ""

    except Exception as e:
        print("Mic error:", e)
        return ""


