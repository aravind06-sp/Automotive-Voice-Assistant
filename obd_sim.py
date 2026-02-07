import random

faults = {
    "P0300": "Random engine misfire detected",
    "P0171": "System too lean",
    "P0420": "Catalyst efficiency below threshold",
    "P0115": "Engine coolant temperature sensor fault",
    "P0560": "System voltage malfunction"
}

def read_fault():
    code = random.choice(list(faults.keys()))
    return code, faults[code]
