Fonctionnement des LED de la carte BeagleBone Black
===================================================

:date: 2014-06-13 22:16
:tags: BeagleBone Black, Linux
:author: Nico
:category: Beaglebone Black

La carte BeagleBone Black dispose de 5 LED directement soudées sur la carte et situées de part et d'autres du connecteur RJ45.

.. thumbnail:: /images/BBB_led_thumb.png
   :target: /images/BBB_led.png
   :align: center
   :scale: 50%
   :class: gallery
   :alt: LED sur la carte BeagleBone Black


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


Chacun de ces répertoires contient une série de fichiers et notamment un fichier, ``trigger`` qui indique le mode de fonctionnement de chaque LED. Sur l'exemple ci-dessous la valeur entre ``[]``, ``hearbeat``, indique que la LED ``USER0`` est configurée comme indicateur de vie du système.

.. code-block:: bash

  root@arm# cd beaglebone\:green\:usr0
  root@arm# ll
  total 0
  drwxr-xr-x 3 root root 0 Jan 1 2000 ./
  drwxr-xr-x 6 root root 0 Jan 1 2000 ../
  -rw-r--r-- 1 root root 4096 Jun 19 19:27 brightness
  lrwxrwxrwx 1 root root 0 Jun 19 19:27 device -> ../../../gpio-leds.8/
  -r--r--r-- 1 root root 4096 Jun 19 19:27 max_brightness
  drwxr-xr-x 2 root root 0 Jun 19 19:27 power/
  lrwxrwxrwx 1 root root 0 Jun 19 19:27 subsystem -> ../../../../../class/leds/
  -rw-r--r-- 1 root root 4096 Jun 19 19:27 trigger
  -rw-r--r-- 1 root root 4096 Jan 1 2000 uevent
  root@arm# cat trigger
  none nand-disk mmc0 mmc1 timer oneshot [heartbeat] backlight gpio cpu0 default-on transient rfkill0 phy0rx phy0tx phy0assoc phy0radio

Il est possible de changer la configuration de la LED simplement en écrivant une nouvelle valeur dans le fichier ``trigger``. Par exemple, pour configurer la LED ``USER0`` en indicateur d'activité du processeur, il suffit de taper les commandes suivantes :

.. code-block:: bash

  root@arm# echo cpu0 > trigger
  root@arm# cat trigger
  none nand-disk mmc0 mmc1 timer oneshot heartbeat backlight gpio [cpu0] default-on transient rfkill0 phy0rx phy0tx phy0assoc phy0radio

La configuration qu'il est possible d'affecter à chaque LED dépend de la version du noyau et des drivers installés, mais voici en gros les principales options :

* ``none`` : désactive l'allumage de la LED
* ``nand-disk`` : indicateur d'accès à la mémoire flash
* ``mmc0`` : indicateur d'accès à la mémoire embarquée eMMC
* ``mmc1`` : indicateur d'accès à la carte SD
* ``timer`` : permet de configurer la LED en mode on/off et de l'allumer ou l'éteindre alternativement. Dans ce mode, deux fichiers ``delay_on`` et ``delay_off`` apparaissent. Ils permettent de configurer les temps (en milli-secondes) d'allumage et d'extinction de la LED
* ``oneshot`` : identique au mode timer, mais chaque cycle on/off est déclenché par l'écriture de données dans le fichier ``shot``
* ``heartbeat`` : indicateur de vie du noyau
* ``cpu0`` : indicateur d'utilisation du processeur
* ``phy*`` : indicateur d'accès au réseau

Il est également possible de désactiver la LED et de la contrôler manuellement :

.. code-block:: bash

  root@arm# echo none > trigger
  root@arm# echo 1 > brightness
  root@arm# echo 0 > brightness

Références :

* `<http://www.valvers.com/embedded-linux/beaglebone/step02-user-led-control>`_
* `<http://www.drdobbs.com/embedded-systems/beaglebone-leds/240001423>`_
* `<http://elinux.org/EBC_Exercise_10_Flashing_an_LED>`_
* `<http://wiki.openwrt.org/doc/uci/system#gpio>`_

