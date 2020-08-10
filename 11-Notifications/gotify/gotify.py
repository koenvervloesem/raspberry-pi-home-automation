"""Post a notification to your Gotify server.

Copyright (C) 2020 Koen Vervloesem

License: MIT
"""
import requests

resp = requests.post(
    "https://HOSTNAME:8443/message?token=APPTOKEN",
    json={
        "message": "Hello from **Python**.",
        "priority": 2,
        "title": "Python notification",
        "extras": {"client::display": {"contentType": "text/markdown"}},
    },
    verify="/home/pi/containers/certificates/rootCA.pem",
)
