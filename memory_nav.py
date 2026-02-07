recent_places = []

def save_place(place):
    if place not in recent_places:
        recent_places.append(place)
    if len(recent_places) > 5:
        recent_places.pop(0)

def get_recent():
    return recent_places
