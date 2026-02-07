import requests

API_KEY = "PASTE_YOUR_GOOGLE_MAPS_KEY"

def get_route(origin, destination):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={API_KEY}"
    data = requests.get(url).json()

    if data["status"] != "OK":
        return "Unable to fetch route"

    steps = data["routes"][0]["legs"][0]["steps"]

    directions = []
    for step in steps[:5]:
        directions.append(step["html_instructions"])

    return " then ".join(directions)
