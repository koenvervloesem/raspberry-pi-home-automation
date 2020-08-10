"""Send an MQTT message with the time to your broker when asked.

Copyright (C) 2020 Koen Vervloesem

License: MIT
"""
import mqttapi as mqtt

MQTT_MSG = "MQTT_MESSAGE"
MQTT_TOPIC_TIME_REQUEST = "time/request"
MQTT_TOPIC_TIME_REPLY = "time/reply"
TIME_FORMAT = "%Y-%m-%d %H:%M"


class TimeApp(mqtt.Mqtt):
    """App that sends the time as an MQTT message."""

    def initialize(self):
        """Subscribe to the right MQTT topic."""
        self.set_namespace("mqtt")
        self.listen_event(
            self.on_time_request, event=MQTT_MSG, topic=MQTT_TOPIC_TIME_REQUEST
        )
        self.log("Time app initialized")

    def on_time_request(self, event_name, data, kwargs):
        """Reply with the time if it's asked."""
        now = self.datetime().strftime(TIME_FORMAT)
        self.mqtt_publish(MQTT_TOPIC_TIME_REPLY, now)
