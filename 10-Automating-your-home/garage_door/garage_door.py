"""Send an MQTT message to your broker when the position of your
garage door changes.

Copyright (C) 2020 Koen Vervloesem

License: MIT
"""
import mqttapi as mqtt

MQTT_MSG = "MQTT_MESSAGE"
MQTT_TOPIC_ACCEL = "bt-mqtt-gateway/ruuvitag/tag2/acceleration_z"
MQTT_TOPIC_STATE = "garagedoor/state"


class GarageDoor(mqtt.Mqtt):
    """App that signals the position of your garage on MQTT."""

    def initialize(self):
        """Subscribe to the right MQTT topic."""
        self.set_namespace("mqtt")
        self.state = "error"
        self.listen_event(self.on_accel, event=MQTT_MSG, topic=MQTT_TOPIC_ACCEL)
        self.log("Garage door app initialized")

    def change_and_publish_if_not(self, state):
        """Change and publish the garage door's state
        if the current state is not equal to the state.
        Do nothing in the other situation.
        """
        if self.state != state:
            self.state = state
            self.mqtt_publish(MQTT_TOPIC_STATE, state)

    def on_accel(self, event_name, data, kwargs):
        """Publish the garage door's state when it changes."""
        acceleration_z = int(data["payload"])
        if acceleration_z > 100:
            self.log("Right side up")
            self.change_and_publish_if_not("error")
        elif acceleration_z < -100:
            self.log("Upside down")
            self.change_and_publish_if_not("open")
        else:
            self.log("On its side")
            self.change_and_publish_if_not("closed")
