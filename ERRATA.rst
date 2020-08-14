######
Errata
######

These are corrections of errors found in the book `Control Your Home with Raspberry Pi: Secure, Modular, Open-Source and Self-sufficient <https://koen.vervloesem.eu/books/control-your-home-with-raspberry-pi/>`_ only after its publication:

*********************************************
Chapter 3: Secure your home automation system
*********************************************

* page 76: The ``docker-compose restart`` command should be ``docker-compose up -d`` so the containers are *recreated* from the new images, not only *restarted* (which they are then from the old images).
* page 77: The sentence "If you have created virtual environments, you have to do repeat the same actions" should be "If you have created virtual environments, you have to repeat the same actions".
