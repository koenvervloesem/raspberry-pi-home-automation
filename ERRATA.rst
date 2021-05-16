######
Errata
######

These are corrections of errors found in the book `Control Your Home with Raspberry Pi: Secure, Modular, Open-Source and Self-sufficient <https://koen.vervloesem.eu/books/control-your-home-with-raspberry-pi/>`_ only after its publication:

********************************************************
Chapter 2: The Raspberry Pi as a home automation gateway
********************************************************

* page 48: If the command to install Docker Compose fails with a message about ``libffi``, first install this dependency with ``sudo apt install libffi-dev``.
* page 50: Due to `a bug <https://github.com/moby/moby/issues/40734>`_ in libseccomp2, the ``python:3.8-alpine`` Docker image fails on the 32-bit version of Raspberry Pi OS Buster. One solution is to change the image to ``python:3.9-slim-buster``. This is fixed in the `docker-compose file in this repository <https://github.com/koenvervloesem/raspberry-pi-home-automation/blob/master/02-The-Raspberry-Pi-as-a-home-automation-gateway/python/docker-compose.yml>`_.

*********************************************
Chapter 3: Secure your home automation system
*********************************************

* page 76: The ``docker-compose restart`` command should be ``docker-compose up -d`` so the containers are *recreated* from the new images, not only *restarted* (which they are then from the old images).
* page 77: The sentence "If you have created virtual environments, you have to do repeat the same actions" should be "If you have created virtual environments, you have to repeat the same actions".

*****************************************************
Chapter 4: MQTT (Message Queuing Telemetry Transport)
*****************************************************

* page 84: Since the release of Mosquitto 2.0, the ``mosquitto.conf`` configuration file needs a line ``allow_anonymous true`` if you want to allow connections without username and password. This is fixed in the `file in this repository <https://github.com/koenvervloesem/raspberry-pi-home-automation/blob/master/04-MQTT/mosquitto/mosquitto.conf>`_.

*********************
Chapter 7: 433.92 MHz
*********************

* page 161: The line ``service:`` in ``docker-compose.yml`` should be ``services:``. Because the ``rtl_433`` project now recommends the Docker container `hertzg/rtl_433 <https://github.com/hertzg/rtl_433_docker>`_, you should change the image. Because there's currently `an issue with the Alpine 3.13 based image whttps://github.com/hertzg/rtl_433_docker/issues/3>`_, use the image ``hertzg/rtl_433:alpine-3.12-latest``. The new image requires a change to the first volume: this should be ``./containers/rtl433tomqtt:/etc/rtl_433:ro``. All this is fixed in the `file in this repository <https://github.com/koenvervloesem/raspberry-pi-home-automation/blob/master/07-433.92-MHz/rtl433tomqtt/docker-compose.yml>`_.
* page 162: Make sure to check the output of the ``lsusb`` command before you enter the values for the ``idVendor`` and ``idProduct`` attributes in the ``udev`` rule: they should match your device. For instance if you see ``ID 0bda:2832`` on the line of your RTL-SDR stick, you need ``ATTRS{idVendor}=="0bda", ATTRS{idProduct}=="2832"`` in the ``udev`` rule.
* page 165: The sentence "You can find see this with:" below the orange box should be "You can see this with:".

*************************
Chapter 12: Voice control
*************************

* page 257: Currently the ReSpeaker drivers aren't compatible with recent kernel versions of Raspberry Pi OS. If the installation of the drivers with ``sudo ./install.sh`` fails, one solution is to clone the fork https://github.com/HinTak/seeed-voicecard/ instead of https://github.com/respeaker/seeed-voicecard and install this one. Hopefully these changes will be merged back in the official repository soon.
