Features
########

:date: 2013-09-01 22:43
:author: Nico
:section: topbar-first
:summary: List of major features
:icon: icon-signal
:order: 1

.. raw:: html

  <div class="alert alert-warning">
  This page is under construction.
  </div>


BrewBox
=======

Hardware
~~~~~~~~

Brewbox hardware includes all design schemas, PCB layout and documentation needed to build an automated brewery. Hardware mostly consists of a single-board computer (possibly `Raspberry Pi <http://www.raspberrypi.org/>`_ or `BeagleBone Black <http://beagleboard.org/Products/BeagleBone%20Black>`_) and an extension board plugged to it. The extension board provides different types of I/O ports like 5V, 12V,110-220VAC (both digital or analog), `I2C <http://en.wikipedia.org/wiki/I2C>`_ or `1-wire <http://en.wikipedia.org/wiki/1-Wire>`_. All these ports can be used for monitoring sensors and controling actuators like temperatures probes, valves or heating element.

Software
~~~~~~~~
Brewbox also comes with a dedicated software for driving the extension board. At the lowest level, this software manages output ports states, collect and translate input values. At a higher level the software uses all these data to report sensor informations and allow actuator controling.

FactoryManager
==============

FactoryManager provides a lightweight ERP software for managing the whole homebrewing activity. Features are still to be defined but this includes stock, purchases, sales, production and customer management.
