"""Custom functions for mqttwarn.

Copyright (C) 2020 Koen Vervloesem

License: MIT
"""
import json

# Data mapping functions


def translate_xiaomi_aqara_contact(topic, data, srv=None):
    """Translate the Xiaomi Aqara's contact sensor JSON data to a
    human-readable description of whether it's open or closed."""
    payload = json.loads(data["payload"])
    if "contact" in payload:
        if payload["contact"]:
            return dict(status="closed")
        else:
            return dict(status="opened")

    return None
