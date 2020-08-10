"""Tell the time when someone asks for it using Rhasspy's Hermes API.

Copyright (C) 2020 Koen Vervloesem

License: MIT
"""
import json

import mqttapi as mqtt

MQTT_MSG = "MQTT_MESSAGE"
INTENT_GETTIME = "hermes/intent/GetTime"
TTS_SAY = "hermes/tts/say"
TIME_FORMAT = "%H %M"


class WhatsTheTime(mqtt.Mqtt):
    """Rhasspy app that tells the time."""

    def initialize(self):
        """Initialize the app by subscribing to the right intent."""
        self.set_namespace("mqtt")
        self.listen_event(self.on_time_request, event=MQTT_MSG, topic=INTENT_GETTIME)
        self.log("What's The Time app initialized")

    def on_time_request(self, event_name, data, kwargs):
        """Tell the time."""
        nlu_payload = json.loads(data["payload"])
        site_id = nlu_payload["siteId"]
        now = self.datetime().strftime(TIME_FORMAT)
        sentence = f"It's {now}."
        self.mqtt_publish(TTS_SAY, json.dumps({"text": sentence, "siteId": site_id}))
