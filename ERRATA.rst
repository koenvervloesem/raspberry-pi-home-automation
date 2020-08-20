######
Errata
######

These are corrections of errors found in the book `Control Your Home with Raspberry Pi: Secure, Modular, Open-Source and Self-sufficient <https://koen.vervloesem.eu/books/control-your-home-with-raspberry-pi/>`_ only after its publication:

*********************************************
Chapter 3: Secure your home automation system
*********************************************

* page 76: The ``docker-compose restart`` command should be ``docker-compose up -d`` so the containers are *recreated* from the new images, not only *restarted* (which they are then from the old images).
* page 77: The sentence "If you have created virtual environments, you have to do repeat the same actions" should be "If you have created virtual environments, you have to repeat the same actions".

*************************
Chapter 12: Voice control
*************************

* page 257: Currently the ReSpeaker drivers aren't compatible with recent kernel versions of Raspberry Pi OS. If the installation of the drivers with ``sudo ./install.sh`` fails, one solution is to clone the fork https://github.com/HinTak/seeed-voicecard/ instead of https://github.com/respeaker/seeed-voicecard and install this one. Hopefully these changes will be merged back in the official repository soon.
