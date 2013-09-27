BrewBox
#######

:date: 2013-09-07 16:29
:title: BrewBox features
:author: Nico
:section: features
:summary: BrewBox consists of hardware and software components combined together to monitor and control a home brewery
:keywords: BrewBox, monitoring, controlling, automation, DIY, home brewing, beaglebone
:icon: icon-signal
:order: 1

Direct access to feature sections :

- `Monitoring`_
- `Control`_

Monitoring
==========

Home brewery monitoring means watching different kind of physical quantities which are important during the brewing process like mash steps temperature, boiling control or liquid flow rate. BrewBox helps you in this task by providing an *hardware interface with sensors fitted in your brewery and a software to process data collected from these sensors*.

Hardware interface
------------------

BrewBox hardware is mostly an interface between electronic sensors fitted in a home brewery and BrewBox software used to monitor it. To be able to work with a wide range of sensors BrewBox hardware supports to following inputs types :

- *5V to 12V analog inputs* for active and passive sensors converting physical quantities to analog electric signals like temperature probes or thermocouples
- *digital inputs* for sensors converting physical quantities to electric pulses like flow transmitter, or on/off sensors like buttons or switches
- `I2C <http://en.wikipedia.org/wiki/I2C>`_ , `SPI <http://en.wikipedia.org/wiki/SPI>`_ and `1-wire <http://en.wikipedia.org/wiki/1-Wire>`_ bus for sensors converting physical quantities to digital signal.

Physically, *BrewBox hardware consists of an expansion board* plugged to a `BeagleBone Black (BBB) <http://beagleboard.org/Products/BeagleBone%20Black>`_ using the board GPIO interface. Additionally with a large choice on inputs, BrewBox hardware also provide power supply management and onboard monitoring for the board itself.

.. image:: /static/images/arch_schema1.png
   :alt: BrewBox architecture diagram
   :align: center



Monitoring software
-------------------

BrewBox software collects and convert data coming from sensors through the hardware interface. All the data collected are used to monitor the brewery activity by :

- building real time or history graphs for some physical quantities measured by sensors
- compare physical quantities to expected values (for example mash steps temperature)
- trigger alert when some value reach some limit
- storing data collected for afterwards analysis or brewing batches comparison.

BrewBox software is also in charge of driving the hardware board and setting inputs mapping to sensors.

BrewBox is written in `Python language <http://www.python.org>`_ and runs on the BeagleBone Black.

.. image:: /static/images/arch_schema2.png
   :alt: BrewBox architecture diagram
   :align: center

Control
=======

Hardware interface
------------------

Home brewery controling means acting on the brewery equipments in order to go through brewing steps like heating the boil kettle or transfering the mash. Actions can be manual (switching on a pump, lighting a gaz burner, etc.) or automated. This is where BrewBox helps. Besides hardware inputs, BrewBox hardware therefore provides several output types in order to drive brewery actuators :

- *5V to 12V digital outputs* used to drive on/off actuators like valves or LED
- *5V to 12V DC outputs* with `Pulse Width Modulation (PWM) <http://en.wikipedia.org/wiki/Pulse-width_modulation>`_. These outputs can be used to drive and control pump speed
- *110V or 220V AC* outputs for high voltage actuators. Control is available in two modes :

  - `solid-state relay <http://en.wikipedia.org/wiki/Solid-state_relay>`_ for on/off actuator
  - PWM for heater power modulation for example.

Software
--------

As for monitoring BrewBox software will drive the hardware interface outputs to control brewery actuators. Values or states sent to outputs will depend on programmatic setup. Brewer will be able to :

- manually set the state or value of some outputs
- automatically trigger state change or value on physical quantity change
- automatically trigger state change or value on timer
- drive outputs with a software `PID controller <http://en.wikipedia.org/wiki/PID_controller>`_.

