##############################
Additional tips and references
##############################

These are some additional tips and references to interesting projects not mentioned in the book `Control Your Home with Raspberry Pi: Secure, Modular, Open-Source and Self-sufficient <https://koen.vervloesem.eu/books/control-your-home-with-raspberry-pi/>`_:

***************************
Integrating other protocols
***************************

The book dives into a specific set of home automation protocols, but the architecture is general and modular enough to use it with other protocols. I found the following projects that look interesting if you want to use another protocol (note that I didn't test them):

digitalSTROM
  `digitalstrom-mqtt <https://github.com/gaetancollaud/digitalstrom-mqtt>`_ lets you set and react to any digitalSTROM devices using MQTT. There's a Docker image on Docker Hub.
KNX
  `knx-mqtt-bridge <https://github.com/pakerfeldt/knx-mqtt-bridge>`_ bridges your KNX devices with MQTT. It doesn't have a Docker image on Docker Hub, but it supplies a Dockerfile to build your own Docker image.
Loxone
  `PyLoxone <https://github.com/JoDehli/PyLoxone>`_ is Home Assistant's binding for Loxone. If you use Home Assistant's Loxone integration and enable `MQTT Statestream <https://www.home-assistant.io/integrations/mqtt_statestream/>`_, state changes of your Loxone devices will also be published as MQTT messages. Another option is using `LoxBerry <https://www.loxwiki.eu/pages/viewpage.action?pageId=27100273>`_ with its MQTT integration.

*****************************************************
Chapter 4: MQTT (Message Queuing Telemetry Transport)
*****************************************************

* `Homie <https://homieiot.github.io/>`_: An MQTT convention for the Internet of Things, defining a standardized way for IoT devices and services to announce themselves and publish their data to the MQTT broker. It seems to be a more detailed specification than `mqtt-smarthome <https://github.com/mqtt-smarthome/>`_, which is mentioned in the book.
* `system_sensors <https://github.com/Sennevds/system_sensors>`_: A Python script that sends system data such as CPU temperature, CPU, disk and memory usage, Wi-Fi signal strength and the number of pending updates over MQTT. Originally created for the Raspberry Pi, but now also works on other Linux systems. If you have MQTT discovery enabled in Home Assistant (see page 221 of the book), you don't need to configure anything in Home Assistant to see the data.
* `serial2mqtt <https://github.com/vortex314/serial2mqtt>`_: A gateway that reads commands from the serial port of a Raspberry Pi and transfers them as MQTT messages to your MQTT broker. For instance, an Arduino board connected to your Raspberry Pi can run ``Serial.println("[1,\"src/myTopic/time\","+String(millis())+"]");`` to publish its uptime to the MQTT topic ``src/myTopic/time``.

*****************
Chapter 9: Zigbee
*****************

* Using the CC2652 instead of the CC2531: In the book I used the CC2531 to create a Zigbee coordinator, but recently two interesting CC2652-based devices have appeared, and both are `supported by Zigbee2mqtt <https://www.zigbee2mqtt.io/information/supported_adapters.html>`_. There's the `Electrolama zig-a-zig-ah! <https://electrolama.com/projects/zig-a-zig-ah/>`_ and `slaesh's CC2652RB stick <https://slae.sh/projects/cc2652/>`_. Both USB adapters have an external antenna and thus a very good range, and they easily handle a Zigbee network of 100+ devices. In contrast to the CC2531, they don't require additional hardware to flash.
* In the book I generated a network key with a complex command. In the mean time, Zigbee2MQTT has implemented an easier way: just add ``network_key: GENERATE`` to the ``advanced`` section in Zigbee2MQTT's ``configuration.yaml``, and the next startup of the container it generates a random network key.

********************************
Chapter 10: Automating your home
********************************

* `ESPHome <https://esphome.io>`_: A project that lets you create firmware for an ESP32 or ESP8266 device not by *programming* but by *configuring*. I wrote a book about it, `Getting Started with ESPHome: Develop your own custom home automation devices <https://koen.vervloesem.eu/books/getting-started-with-esphome/>`_. I find this the perfect companion for the home automation system of the book *Control your home with Raspberry Pi*. The devices you create with ESPHome connect to your MQTT broker but they can also work completely autonomously.
* `Homepoint <https://github.com/sieren/Homepoint>`_: Firmware to turn an ESP32-based device such as the M5Stack Core into a dashboard for an MQTT-based home automation system. I wrote a blog post about it, including a configuration example: `Create a dashboard for your MQTT-based home automation system with the M5Stack Core and Homepoint <https://koen.vervloesem.eu/blog/create-a-dashboard-for-your-mqtt-based-home-automation-system-with-the-m5stack-core-and-homepoint/>`_.
* `RuuviTag Demo <https://github.com/koenvervloesem/ruuvitag-demo>`_: In this demo Telegraf collects MQTT messages with RuuviTag sensor measurements from bt-mqtt-gateway, sends the values to InfluxDB where they are stored in a time-series database, and then shows them in a Grafana dashboard. I haven't covered Grafana in the book, but you should definitely check it out when you want some more powerful dashboard functionality.

*************************
Chapter 12: Voice control
*************************

* `Automatically save the volume of your ReSpeaker 2-Mics Pi HAT <https://koen.vervloesem.eu/blog/automatically-save-the-volume-of-your-respeaker-2-mics-pi-hat/>`_: A solution I found to the (sometimes not so) minor annoyance that the playback volume of the ReSpeaker 2-Mics Pi HAT is reset to its maximal value after each reboot.
