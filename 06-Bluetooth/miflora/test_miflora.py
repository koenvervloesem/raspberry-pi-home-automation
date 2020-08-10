"""Show some measurements of a Xiaomi Mi Flora plant sensor.

Copyright (C) 2020 Koen Vervloesem

License: MIT
"""
from btlewrap.bluepy import BluepyBackend
from miflora.miflora_poller import MiFloraPoller

MAC = "C4:7C:8D:67:65:AD"
POLLER = MiFloraPoller(MAC, BluepyBackend)

print("Temperature; " + str(POLLER.parameter_value("temperature")))
print("Moisture: " + str(POLLER.parameter_value("moisture")))
print("Light: " + str(POLLER.parameter_value("light")))
print("Conductivity: " + str(POLLER.parameter_value("conductivity")))
print("Battery: " + str(POLLER.parameter_value("battery")))
