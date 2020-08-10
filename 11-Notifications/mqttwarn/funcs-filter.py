# Data mapping functions


def zigbee2mqtt_device_name(topic, data, srv=None):
    """Return the last part of the MQTT topic name."""
    return dict(name=topic.split("/")[-1])


# Filter functions


def filter_xiaomi_aqara_battery_low(topic, message):
    """Ignore messages from Xiaomi Aqara when the battery is OK."""
    data = json.loads(message)
    if "battery" in data:
        return int(data["battery"]) > 20

    return True
