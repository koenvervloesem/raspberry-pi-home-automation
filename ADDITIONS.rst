##############################
Additional tips and references
##############################

These are some additional tips and references to interesting projects not mentioned in the book `Control Your Home with Raspberry Pi: Secure, Modular, Open-Source and Self-sufficient <https://koen.vervloesem.eu/books/control-your-home-with-raspberry-pi/>`_:

***************************
Integrating other protocols
***************************

The book dives into a specific set of home automation protocols, but the architecture is general and modular enough to use it with other protocols. I found the following projects that look interesting if you want to use another protocol (note that I didn't test them):

KNX
  `knx-mqtt-bridge <https://github.com/pakerfeldt/knx-mqtt-bridge>`_ bridges your KNX devices with MQTT. It doesn't have a Docker image on Docker Hub, but it supplies a Dockerfile to build your own Docker image.
Loxone
  `PyLoxone <https://github.com/JoDehli/PyLoxone>`_ is Home Assistant's binding for Loxone. If you use Home Assistant's Loxone integration and enable `MQTT Statestream <https://www.home-assistant.io/integrations/mqtt_statestream/>`_, state changes of your Loxone devices will also be published as MQTT messages. Another option is using `LoxBerry <https://www.loxwiki.eu/pages/viewpage.action?pageId=27100273>`_ with its MQTT integration.

*************************
Chapter 12: Voice control
*************************

* `Automatically save the volume of your ReSpeaker 2-Mics Pi HAT <https://koen.vervloesem.eu/blog/automatically-save-the-volume-of-your-respeaker-2-mics-pi-hat/>`_: A solution I found to the (sometimes not so) minor annoyance that the playback volume of the ReSpeaker 2-Mics Pi HAT is reset to its maximal value after each reboot.
