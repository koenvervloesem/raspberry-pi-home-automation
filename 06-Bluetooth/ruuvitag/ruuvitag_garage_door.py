"""Send an MQTT message when the position of your garage door changes.

Copyright (C) 2020 Koen Vervloesem

License: MIT
"""
from threading import Thread

import paho.mqtt.client as mqtt
from ruuvitag_sensor.ruuvi import RuuviTagSensor

MQTT_HOST = "HOSTNAME"
MQTT_PORT = 8883
MQTT_CAFILE = "/path/to/rootCA.pem"
MQTT_USERNAME = "home"
MQTT_PASSWORD = "PASSWORD"
MQTT_CLIENT_ID = "RuuviTagGarageDoor"

MQTT_TOPIC = "garagedoor/state"
MAC = "C8:03:24:74:7E:0E"


def handle_data(found_data):
    """Handle acceleration data from the RuuviTag sensor."""
    global state
    acceleration_z = found_data[1]["acceleration_z"]
    if acceleration_z > 100:
        print("Right side up")
        if state != "error":
            state = "error"
            mqtt_client.publish(MQTT_TOPIC, "error")
    elif acceleration_z < -100:
        print("Upside down")
        if state != "open":
            state = "open"
            mqtt_client.publish(MQTT_TOPIC, "open")
    else:
        print("On its side")
        if state != "closed":
            state = "closed"
            mqtt_client.publish(MQTT_TOPIC, "closed")


def on_connect(client, userdata, flags, rc):
    """Start receiving RuuviTag sensor data after connecting."""
    print("Connected with result code " + str(rc))
    Thread(
        target=RuuviTagSensor.get_datas, args=(handle_data, [MAC]), daemon=True
    ).start()


if __name__ == "__main__":
    # Initialize program state and MQTT connection
    state = "error"
    mqtt_client = mqtt.Client(MQTT_CLIENT_ID)
    mqtt_client.on_connect = on_connect

    # Set up authentication and TLS encryption
    mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    mqtt_client.tls_set(ca_certs=MQTT_CAFILE)

    # Connect and start event loop
    mqtt_client.connect(MQTT_HOST, MQTT_PORT)
    mqtt_client.loop_forever()
