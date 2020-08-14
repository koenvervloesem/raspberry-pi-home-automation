###################################
Control Your Home with Raspberry Pi
###################################

This repository contains the code discussed in the book `Control Your Home with Raspberry Pi: Secure, Modular, Open-Source and Self-sufficient <https://koen.vervloesem.eu/books/control-your-home-with-raspberry-pi/>`_, published by `Elektor International Media <https://www.elektor.com>`_, as well as a list of errors and their corrections.

**************
About the book
**************

Ever since the Raspberry Pi was introduced, it has been used by enthusiasts to automate their homes. The Raspberry Pi is a powerful computer in a small package, with lots of interfacing options to control various devices.

This book shows you how you can automate your home with a Raspberry Pi. You'll learn how to use various wireless protocols for home automation, such as Bluetooth, 433.92 MHz radio waves, Z-Wave, and Zigbee. Soon you'll automate your home with Python, Node-RED, and Home Assistant, and you'll even be able to speak to your home automation system.

All this is done securely, with a modular system, completely open-source, without relying on third-party services. You're in control of your home, and no one else.

At the end of this book, you can install and configure your Raspberry Pi as a highly flexible home automation gateway for protocols of your choice, and link various services with MQTT to make it your own system. This DIY (do it yourself) approach is a bit more laborious than just installing an off-the-shelf home automation system, but in the process, you can learn a lot, and in the end, you know exactly what's running your house and how to tweak it. This is why you were interested in the Raspberry Pi in the first place, right?

* Turn your Raspberry Pi into a reliable gateway for various home automation protocols.
* Make your home automation setup reproducible with Docker Compose.
* Secure all your network communication with TLS.
* Create a video surveillance system for your home.
* Automate your home with Python, Node-RED, Home Assistant and AppDaemon.
* Securely access your home automation dashboard from remote locations.
* Use fully offline voice commands in your own language.

+----------------------+-------------------------------------+
| **Title**            | Control Your Home with Raspberry Pi |
+----------------------+-------------------------------------+
| **Author**           | Koen Vervloesem                     |
+----------------------+-------------------------------------+
| **Publication date** | 2020-08-17                          |
+----------------------+-------------------------------------+
| **Number of pages**  | 331                                 |
+----------------------+-------------------------------------+
| **Price**            | € 37.50                             |
+----------------------+-------------------------------------+
| **ISBN-13**          | 978-1-907920-94-3                   |
+----------------------+-------------------------------------+
| **ISBN-10**          | 1-907920-94-3                       |
+----------------------+-------------------------------------+
| **Publisher**        | Elektor International Media (EIM)   |
+----------------------+-------------------------------------+

*************
Included code
*************

This code, organized by chapter, includes:

* Docker Compose files to start the discussed services as Docker containers. Note that in most of these Docker Compose files you have to add the ``mosquitto`` service. In practice you copy the services from various Docker Compose files and add them to one Docker Compose file to run your whole home automation stack.
* Configuration files for various services. Some of these are fragments of configuration files. Read the relevant chapter for an explanation of these configuration fragments.
* Python scripts, some of them meant to be run in AppDaemon.

*****************
Download the code
*****************

You can download the code on your Raspberry Pi all at once with:

.. code-block:: shell

  git clone https://github.com/koenvervloesem/raspberry-pi-home-automation.git

You may need to install ``git`` first:

.. code-block:: shell

  sudo apt install git

The code is then downloaded into the directory ``raspberry-pi-home-automation``, organized by chapter.

If you prefer to download only a specific file, navigate to the file in GitHub's web interface and then click on **Raw** at the right. Then copy the URL from your web browser's URL bar and paste it after the ``wget`` command, for instance:

.. code-block:: shell

  wget https://github.com/koenvervloesem/raspberry-pi-home-automation/blob/master/12-Voice-control/rhasspy/sentences.ini

Make sure that you're in the right directory first, or move the file to the correct location afterwards.

Just selecting and copying the code from the web interface and pasting it in an editor may also work, but is not recommended. Especially with Python code the whitespace can become mixed up, which results in invalid code.

******
Errata
******

See the `ERRATA <ERRATA.rst>`_ document for the list of errors in the book and their corrections.

*******
License
*******

All code is provided by `Koen Vervloesem <http://koen.vervloesem.eu>`_ as open source software with the MIT license. See the `LICENSE <LICENSE>`_ for more information.
