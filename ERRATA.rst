######
Errata
######

These are corrections of errors found in the book `Control Your Home with Raspberry Pi: Secure, Modular, Open-Source and Self-sufficient <https://koen.vervloesem.eu/books/control-your-home-with-raspberry-pi/>`_ only after its publication:

********************************************************
Chapter 2: The Raspberry Pi as a home automation gateway
********************************************************

* page 29: "Compute Model 3" at the bottom of the page should be "Compute Module 3".
* page 40: The ``raspi-config`` menu options have changed. The hostname is now in **1 System Options - S4 Hostname**. The timezone is in **5 Localisation Options - L2 Timezone**. The memory split has moved to **4 Performance Options - P2 GPU Memory**.
* page 48: Installing Docker as in section 2.9.1 now automatically installs Docker Compose, so you don't need to install it anymore with pip. If not, you can still install Docker Compose manually with ``sudo apt install docker-compose-plugin``. Note that with this new plugin, you need to run the command as ``docker compose``, not ``docker-compose``.
* page 50: Due to `a bug <https://github.com/moby/moby/issues/40734>`_ in libseccomp2, the ``python:3.8-alpine`` Docker image fails on the 32-bit version of Raspberry Pi OS Buster. One solution is to change the image to ``python:3.9-slim-buster``. This is fixed in the `docker-compose file in this repository <https://github.com/koenvervloesem/raspberry-pi-home-automation/blob/master/02-The-Raspberry-Pi-as-a-home-automation-gateway/python/docker-compose.yml>`_.

*********************************************
Chapter 3: Secure your home automation system
*********************************************

* page 69: The sentence "The window you're seeing now is the Certificate Manager." should be "The window you're seeing now is the Certificate Manager, and you need its tab Authorities."
* page 71: Figure 3.10 should be `another figure <https://github.com/koenvervloesem/raspberry-pi-home-automation/blob/master/images/3.10-mkcert-certificate.png>`_, showing the ``./mkcert pi-red.home pi-red`` command.
* page 76: The ``docker-compose restart`` command should be ``docker-compose up -d`` so the containers are *recreated* from the new images, not only *restarted* (which they are then from the old images).
* page 77: The sentence "If you have created virtual environments, you have to do repeat the same actions" should be "If you have created virtual environments, you have to repeat the same actions".

*****************************************************
Chapter 4: MQTT (Message Queuing Telemetry Transport)
*****************************************************

* page 84: Since the release of Mosquitto 2.0, the ``mosquitto.conf`` configuration file needs a line ``allow_anonymous true`` if you want to allow connections without username and password. Moreover, the ``port`` option is now deprecated and should be changed to the ``listener`` option (also on page 86 and 101). All this is fixed in the `Mosquitto configuration files in this repository <https://github.com/koenvervloesem/raspberry-pi-home-automation/tree/master/04-MQTT/mosquitto>`_.
* page 93: MQTT.fx is no longer free. An open-source alternative with roughly the same functionality is `mqttk <https://github.com/matesh/mqttk>`_. You can install it from PyPI using ``pip3 install mqttk`` and it works on Windows, macOS and Linux.

********************
Chapter 6: Bluetooth
********************

* page 150: The location of the configuration file of ``bt-mqtt-gateway`` in its Docker container has changed from ``/config.yaml`` to ``/application/config.yaml``. This has been fixed in the `docker-compose file in this repository <https://github.com/koenvervloesem/raspberry-pi-home-automation/blob/master/06-Bluetooth/bt-mqtt-gateway/docker-compose.yml>`_.

*********************
Chapter 7: 433.92 MHz
*********************

* page 161: The line ``service:`` in ``docker-compose.yml`` should be ``services:``. Because the ``rtl_433`` project now recommends the Docker container `hertzg/rtl_433 <https://github.com/hertzg/rtl_433_docker>`_, you should change the image. Because there's currently `an issue with the Alpine 3.13 based image <https://github.com/hertzg/rtl_433_docker/issues/3>`_, use the image ``hertzg/rtl_433:alpine-3.12-latest``. The new image requires a change to the first volume: this should be ``./containers/rtl433tomqtt:/etc/rtl_433:ro``. All this is fixed in the `file in this repository <https://github.com/koenvervloesem/raspberry-pi-home-automation/blob/master/07-433.92-MHz/rtl433tomqtt/docker-compose.yml>`_.
* page 162: Make sure to check the output of the ``lsusb`` command before you enter the values for the ``idVendor`` and ``idProduct`` attributes in the ``udev`` rule: they should match your device. For instance if you see ``ID 0bda:2832`` on the line of your RTL-SDR stick, you need ``ATTRS{idVendor}=="0bda", ATTRS{idProduct}=="2832"`` in the ``udev`` rule.
* page 165: The sentence "You can find see this with:" below the orange box should be "You can see this with:".

*****************
Chapter 9: Zigbee
*****************

* page 193: Zigbee2MqttAssistant isn't maintained anymore. Zigbee2MQTT has its own `frontend <https://www.zigbee2mqtt.io/guide/configuration/frontend.html#nginx-proxy-configuration>`_ now with a web interface for your Zigbee devices. Consult its documentation for the configuration. You can remove the ``zigbee2mqttassistant`` container from the book's Docker Compose file.
* page 197: In the book I generate the Zigbee network key with a complex command. In the mean time, Zigbee2MQTT has implemented an easier way: just add ``network_key: GENERATE`` to the ``advanced`` section in Zigbee2MQTT's ``configuration.yaml``. The next startup of the container it generates a random network key.

********************************
Chapter 10: Automating your home
********************************

* page 205: The command to generate a password hash in the Node-RED container still works, but since Node-RED 1.1.0 you can also use the easier command ``docker exec -ti node-red node-red admin hash-pw`` (the former occurrence of ``node-red`` is the container name, the latter the name of the command).

*************************
Chapter 12: Voice control
*************************

* page 257: Currently the ReSpeaker drivers aren't compatible with recent kernel versions of Raspberry Pi OS. If the installation of the drivers with ``sudo ./install.sh`` fails, one solution is to clone the fork https://github.com/HinTak/seeed-voicecard/ instead of https://github.com/respeaker/seeed-voicecard and install this one. Hopefully these changes will be merged back in the official repository soon.
