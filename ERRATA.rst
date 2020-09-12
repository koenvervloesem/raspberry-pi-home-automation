######
Errata
######

These are corrections of errors found in the book `Control Your Home with Raspberry Pi: Secure, Modular, Open-Source and Self-sufficient <https://koen.vervloesem.eu/books/control-your-home-with-raspberry-pi/>`_ only after its publication:

********************************************************
Chapter 2: The Raspberry Pi as a home automation gateway
********************************************************

* page 48: If the command to install Docker Compose fails with a message about ``libffi``, first install this dependency with ``sudo apt install libffi-dev``.

*********************************************
Chapter 3: Secure your home automation system
*********************************************

* page 76: The ``docker-compose restart`` command should be ``docker-compose up -d`` so the containers are *recreated* from the new images, not only *restarted* (which they are then from the old images).
* page 77: The sentence "If you have created virtual environments, you have to do repeat the same actions" should be "If you have created virtual environments, you have to repeat the same actions".

*********************
Chapter 7: 433.92 MHz
*********************

* page 161: The line ``service:`` in ``docker-compose.yml`` should be ``services:``. This is fixed in the `file in this repository <https://github.com/koenvervloesem/raspberry-pi-home-automation/blob/master/07-433.92-MHz/rtl433tomqtt/docker-compose.yml>`_.

*************************
Chapter 12: Voice control
*************************

* page 257: Currently the ReSpeaker drivers aren't compatible with recent kernel versions of Raspberry Pi OS. If the installation of the drivers with ``sudo ./install.sh`` fails, one solution is to clone the fork https://github.com/HinTak/seeed-voicecard/ instead of https://github.com/respeaker/seeed-voicecard and install this one. Hopefully these changes will be merged back in the official repository soon.
