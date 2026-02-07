# AI Vehicle CoPilot

AI Vehicle CoPilot is a voice-controlled smart assistant for vehicles that helps drivers access important vehicle information, run diagnostics, get navigation assistance, and ask automotive-related questions.

This project demonstrates how Artificial Intelligence, Machine Learning, and voice interfaces can be integrated to build a practical in-car assistant.

---

## What This Project Does

- Listens to voice commands  
- Provides spoken responses  
- Displays live vehicle data such as speed, fuel level, and engine temperature  
- Supports navigation using Google Maps  
- Simulates vehicle fault codes and explains them  
- Answers automotive questions using a local knowledge base  

All processing runs locally using Python.

---

## Technologies Used

- Python  
- Tkinter  
- SpeechRecognition  
- pyttsx3  
- Scikit-learn  
- SentenceTransformers  
- FAISS  

---

## Project Structure

AI-Vehicle-CoPilot/

dashboard.py        - Main dashboard application  
main.py             - Console version  
vehicle_sim.py      - Simulates vehicle sensor data  
intent_model.py     - Detects user intent  
rag_engine.py       - Knowledge retrieval engine  
voice.py            - Speech input/output  
obd_sim.py          - Simulates diagnostic fault codes  
memory_nav.py       - Stores recent navigation places  
knowledge.txt       - Automotive knowledge base  
README.md  

---

## Installation

1. Create a virtual environment (optional but recommended)

python -m venv venv  
venv\Scripts\activate  

2. Install required packages

pip install speechrecognition pyttsx3 scikit-learn sentence-transformers faiss-cpu pyaudio  

---

## Running the Project

Run the GUI dashboard:

python dashboard.py  

Run the console version:

python main.py  

---

## Sample Voice Commands

What is speed  
Check fuel level  
Engine temperature  
Navigate to college  
Run diagnostics  
Why engine overheating  

---

## How It Works

1. Microphone captures user voice  
2. Speech is converted to text  
3. Intent classification model determines the request  
4. Appropriate module processes the request  
5. Response is displayed and spoken  

Knowledge-based queries use vector similarity search over a local knowledge base.

---

## Future Enhancements

- Integration with real OBD-II hardware  
- GPS module support  
- Mobile application  
- Multilingual voice support  
- Edge AI deployment  

---

## Author

Aravindan Sivakumar  
Electrical and Electronics Engineering Student  

---

