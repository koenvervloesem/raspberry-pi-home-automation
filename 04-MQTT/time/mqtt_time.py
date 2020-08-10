"""Send an MQTT message with the time to your broker when asked.

Copyright (C) 2020 Koen Vervloesem

License: MIT
"""
from datetime import datetime

import paho.mqtt.client as mqtt

MQTT_HOST = "HOSTNAME"
MQTT_PORT = 8883
MQTT_CAFILE = "/path/to/rootCA.pem"
MQTT_USERNAME = "home"
MQTT_PASSWORD = "PASSWORD"
MQTT_CLIENT_ID = "Time"

MQTT_TOPIC_TIME_REQUEST = "time/request"
MQTT_TOPIC_TIME_REPLY = "time/reply"

TIME_FORMAT = "%Y-%m-%d %H:%M"


def on_connect(client, userdata, flags, rc):
    """Subscribe to the right MQTT topics after connecting."""
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC_TIME_REQUEST)


def on_message(client, userdata, message):
    """Reply with the time when asked."""
    now = datetime.now().strftime(TIME_FORMAT)
    client.publish(MQTT_TOPIC_TIME_REPLY, now)


if __name__ == "__main__":
    # Initialize MQTT connection
    mqtt_client = mqtt.Client(MQTT_CLIENT_ID)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    # Set up authentication and TLS encryption
    mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    mqtt_client.tls_set(ca_certs=MQTT_CAFILE)

    # Connect and start event loop
    mqtt_client.connect(MQTT_HOST, MQTT_PORT)
    mqtt_client.loop_forever()
