Getting started
###############

:date: 2013-08-25 11:47
:author: Nico
:section: topbar-first
:summary: Beerfactory provides open source software and hardware for managing a homebrewing activity
:icon: icon-play-sign
:order: 0

*This project is in early stage and this page currently describes its goal.*

Beerfactory provides open source `software`_ and `hardware`_ for managing a homebrewing activity.

Hardware
--------
Beerfactory hardware includes all design schemas, PCB layout and documentation needed to build an automated brewery. Hardware mostly consists of a single-board computer (like `Raspberry Pi <http://www.raspberrypi.org/>`_ or `BeagleBone Black <http://beagleboard.org/Products/BeagleBone%20Black>`_) and an extension board plugged to it. The extension board provides different types of I/O ports like 5V, 12V,110-220V (both digital or analog), `I2C <http://en.wikipedia.org/wiki/I2C>`_ or `1-wire <http://en.wikipedia.org/wiki/1-Wire>`_. All these ports can be used for monitoring sensors and controling actuators of any types.

Software
--------
Beerfactory hardware comes with a dedicated software for driving the extension board. At the lowest level, this software manages output ports states, collect and translate input values. At a higher level the software use these data to report sensor informations and allow actuator controling.

Besides this monitoring and controling software, Beerfactory provides a software for managing the whole homebrewing activity. Features are still to be defined but this includes stock, purchases, sales, production and customer management.

What's next ?
-------------

This project is in features and general architecture analysis. Project activity will be reported on the `blog </category/news.html>`_. Anyone interested in this project is welcome to contribute through the `forum <http://forum.beerfactory.org>`_.

