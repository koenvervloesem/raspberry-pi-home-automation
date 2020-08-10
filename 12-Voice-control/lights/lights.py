"""Rhasspy intent handler for the TurnOnLight intent.

Copyright (C) 2020 Koen Vervloesem

License: MIT
"""
import json

import paho.mqtt.client as mqtt

MQTT_HOST = "pi-red"
MQTT_PORT = 1883
MQTT_CLIENT_ID = "Lights"
MQTT_USERNAME = "home"
MQTT_PASSWORD = "PASSWORD"

INTENT_LIGHT = "hermes/intent/TurnOnLight"
INTENT_NOT_RECOGNIZED = "hermes/nlu/intentNotRecognized"
TTS_SAY = "hermes/tts/say"


def on_connect(client, userdata, flags, rc):
    """Subscribe to the right MQTT topics after connecting."""
    print("Connected with result code " + str(rc))
    client.subscribe(INTENT_LIGHT)
    client.subscribe(INTENT_NOT_RECOGNIZED)


def on_message(client, userdata, msg):
    """Called each time an intent is recognized (or not)."""
    nlu_payload = json.loads(msg.payload)
    if msg.topic == INTENT_NOT_RECOGNIZED:
        sentence = "Unrecognized command."
        print("Recognition failure")
    else:
        print("Got intent:", nlu_payload["intent"]["intentName"])
        room_slot = nlu_payload["slots"][0]
        room_name = room_slot["raw_value"]
        sentence = "Turning on {} light.".format(room_name)

    site_id = nlu_payload["siteId"]
    client.publish(TTS_SAY, json.dumps({"text": sentence, "siteId": site_id}))


if __name__ == "__main__":
    # Initialize MQTT connection
    mqtt_client = mqtt.Client(MQTT_CLIENT_ID)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    mqtt_client.connect(MQTT_HOST, MQTT_PORT)

    # Start event loop
    mqtt_client.loop_forever()
