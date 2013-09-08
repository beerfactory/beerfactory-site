BrewBox
#######

:date: 2013-09-07 16:29
:author: Nico
:section: features
:summary: BrewBox features
:keywords: BrewBox, monitoring, controlling, automation, DIY, home brewing, beaglebone
:icon: icon-signal
:order: 1

.. raw:: html

  <div class="alert alert-warning">
  This page is under construction.
  </div>


BrewBox provides hardware and software components for monitoring and controlling a home brewery. Sections below describes BrewBox features in details.


General architecture
~~~~~~~~~~~~~~~~~~~~

BrewBox-hardware provides an interface between a microbrewery electronics equipements and the BrewBox software used to monitor and control the microbrewery. BrewBox-hardware can be used to collects data from sensors installed in a microbewery like temperature sensors, flow sensors or level sensors. It is also used to send commands to the brewery actuators like pumps, valves or heating elements.

BrewBox-hardware mostly consists of a `single-board computer <http://en.wikipedia.org/wiki/Single_board_computer>`_ (like `Raspberry Pi <http://www.raspberrypi.org/>`_ or `BeagleBone Black <http://beagleboard.org/Products/BeagleBone%20Black>`_) and an expansion board plugged to it using a `GPIO <http://en.wikipedia.org/wiki/GPIO>`_ port. The single board computer also hosts Brewbox-software component which interacts with the extension board and the user.

.. raw:: html

  <div class="alert alert-warning">
  TODO : Add a schema
  </div>


Hardware features
~~~~~~~~~~~~~~~~~

The extension board provides different types of I/O ports like 5V, 12V,110-220VAC (both digital or analog), `I2C <http://en.wikipedia.org/wiki/I2C>`_ or `1-wire <http://en.wikipedia.org/wiki/1-Wire>`_. All these ports can be used for monitoring sensors and controling actuators like temperatures probes, valves or heating element.

Brewbox hardware includes all design schemas, PCB layout and documentation needed to build an automated brewery.

Software features
~~~~~~~~~~~~~~~~~

BrewBox-software procceses data coming from the hardware components


Brewbox also comes with a dedicated software for driving the extension board. At the lowest level, this software manages output ports states, collect and translate input values. At a higher level the software uses all these data to report sensor informations and allow actuator controling.