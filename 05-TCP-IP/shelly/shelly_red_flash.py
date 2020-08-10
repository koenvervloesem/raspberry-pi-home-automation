"""Let a Shelly RGBW2 LED controller flash the LEDs red.

Copyright (C) 2020 Koen Vervloesem

License: MIT
"""
import time

import requests

# Define URLs for the Shelly HTTP API
IP = "http://192.168.0.202"
SHELLY = IP + "/shelly"
COLOR = IP + "/color/0/"
DISABLE_EFFECTS = "effect=0"
ONLY_RED = "red=255&green=0&blue=0&white=0"
ON = "turn=on"
OFF = "turn=off"
AUTH = ("admin", "admin")
HEADER = {"Content-Type": "application/x-www-form-urlencoded"}

try:
    shelly = requests.get(SHELLY)
    if shelly.status_code == 200:
        shelly_json = shelly.json()
        shelly_type = shelly_json["type"]
        shelly_mac = shelly_json["mac"]
        print(
            "Connected to device {} with MAC address {}.".format(
                shelly_type, shelly_mac
            )
        )

    # Disable effects and show only red
    disable_effects = requests.post(
        COLOR, auth=AUTH, headers=HEADER, data=DISABLE_EFFECTS
    )
    only_red = requests.post(COLOR, auth=AUTH, headers=HEADER, data=ONLY_RED)

    while True:
        on = requests.post(COLOR, auth=AUTH, headers=HEADER, data=ON)
        time.sleep(1)
        off = requests.post(COLOR, auth=AUTH, headers=HEADER, data=OFF)
        time.sleep(1)
except requests.exceptions.ConnectionError as e:
    print("Can't connect to device {}: {}".format(IP, e))
