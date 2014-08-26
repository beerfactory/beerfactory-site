Fonctionnement des LED de la carte BeagleBone Black
===================================================

:date: 2014-06-13 22:16
:tags: BeagleBone Black, Linux
:author: Nico
:category: Beaglebone Black

La carte BeagleBone Black dispose de 5 LED directement soudées sur la carte et situées de part et d'autres du connecteur RJ45.

.. image:: /images/BBB_led.png
   :alt: LED sur la carte BeagleBone Black
   :align: center

La LED ``POWER`` a peu d'intérêt. Elle indique seulement, lorsqu'elle est allumée, que la carte est correctement alimentée. Les 4 autres LED sont configurables par l'utilisateur, mais elles sont par défaut associées à des fonctions spécifiques. Ainsi, en partant de la droite, ces LED ont normalement les fonctions suivantes :

* ``USER0`` : indicateur de vie (hearbeat) du noyau Linux
* ``USER1`` : indicateur d'entrée/sortie sur la carte microSD
* ``USER2`` : indicateur d'activité du noyau. Plus cette LED est allumée, plus le système est actif
* ``USER3`` : indicateur d'entrée/sortie sur la mémoire embarquée eMMC

La fonction de chaque LED est configurable via l'arborescence ``/sys`` qui contient un répertoire de configuration pour chaque LED:

.. code-block:: bash

  /sys/class/leds/beaglebone:green:usr0/
  /sys/class/leds/beaglebone:green:usr1/
  /sys/class/leds/beaglebone:green:usr2/
  /sys/class/leds/beaglebone:green:usr3/

