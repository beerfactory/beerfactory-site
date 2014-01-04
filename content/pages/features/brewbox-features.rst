BrewBox
#######

:date: 2013-09-07 16:29
:title: BrewBox
:author: Nico
:section: features
:summary: BrewBox est constitué de composants logiciels et matériels permettant de surveiller et contrôler une pico-brasserie
:keywords: BrewBox, monitoring, controlling, automation, DIY, home brewing, beaglebone
:icon: icon-signal
:order: 1

Accès direct aux sections :

- `Surveillance`_
- `Contrôle`_

Surveillance
============

Surveiller une pico-brasserie c'est suivre différentes grandeurs physiques qui sont importantes durant le brassage comme la température des paliers d'empâtage, le contrôle de l'ébullition ou les flux de liquides. BrewBox vous aide dans cette tâche en fournissant une *interface matérielle avec les capteurs équipant la pico-brasserie* et un *logiciel de collecte et d'analyse des données provenant de ces capteurs*.

Interface matérielle
--------------------

L'interface matérielle de BrewBox est principalement une interface électronique entre les capteurs équipant une pico-brasserie et le logiciel BrewBox chargé de la surveiller. BrewBox dispose d'un nombre important d'interface afin de s'interfacer avec un maximum de capteurs :

- *entrées analogiques 5-12V* pour les capteurs actifs ou passifs convertissant les grandeurs physiques en signaux électriques analogiques comme les thermistances ou les thermocouples;
- *entrées numériques* pour les capteurs convertissant les grandeurs physiques en pulsions électriques comme les compteurs ou les boutons ;
- entrées bus `I2C <http://en.wikipedia.org/wiki/I2C>`_ , `SPI <http://en.wikipedia.org/wiki/SPI>`_ et `1-wire <http://en.wikipedia.org/wiki/1-Wire>`_ pur les capteurs interfacés avec ces bus.

Concrètement, *l'interface matérielle de BrewBox est constituée d'une carte d'extension* connectée à un `BeagleBone Black (BBB) <http://beagleboard.org/Products/BeagleBone%20Black>`_. En plus d'un large choix d'entrée/sorties l'interface matérielle de BrewBox fournit également l'alimentation nécessaire ainsi qu'une surveillance de la carte elle-même.

.. image:: /static/images/arch_schema1.png
   :alt: BrewBox architecture diagram
   :align: center


Logiciel
--------

Le logiciel BrewBox collecte et convertit les données provenant des capteurs au travers de l'interface matérielle. Les données collectées permettent de surveiller l'activité de la pico-brasserie :

- tracés en temps réel ou en historique de graphiques des grandeurs physiques mesurées
- comparaison des grandeurs physiques par rapport à des consignes ou des valeurs attendues (par exemple paliers de température d'empâtage)
- déclenchement d'alertes sur dépassement de valeur d'une grandeur physique
- enregistrement des données collectées pour analyse à froid ou comparaison des brassages successifs.

Le logiciel BrewBox est également responsable du pilotage de la carte d'interface et de la configuration matérielle.

BrewBox est écrit en `Python <http://www.python.org>`_ et s'exécute sur le BeagleBone Black.

.. image:: /static/images/arch_schema2.png
   :alt: BrewBox architecture diagram
   :align: center

Contrôle
========

Interface matérielle
--------------------

Le contrôle et l'automatisation d'un pico-brasserie consiste à agir sur les équipements de la pico-brasserie afin de procéder aux différentes étapes du brassage comme chauffer la cuve d'ébullition ou transférer le moût. Ces actions peuvent être manuelles (actionner une vanne, allumer un bruleur, ...) ou automatisées. C'est là que BrewBox intervient : en plus des entrées précédemment décrites BrewBox fournit différents types de sorties permettant de piloter les actionneurs de la pico-brasserie :

- *sorties 5-12V digitales* utilisées pour piloter les actionneurs tout ou rien comme des vannes ou des LED
- *sorties 5-12V* avec `PWM <http://en.wikipedia.org/wiki/Pulse-width_modulation>`_. Ces sorties peuvent par exemple être utilisées pour piloter et contrôler la vitesse d'une pompe
- *sorties 110V ou 220V alternatif* pour les actionneurs de puissance. Les pilotage est disponible en deux modes :

  - `relais SSR <http://en.wikipedia.org/wiki/Solid-state_relay>`_ pour les actionneurs tout ou rien
  - PWM pour la modulation du chauffage par exemple

Logiciel
--------

Le logiciel BrewBox pilote l'interface matériel afin de contrôler l'état des actionneurs. Les consignes transmises aux sorties dépendent des actions de l'utilisateur ou de la programmation effectuée :

- contrôle manuel de l'état de et des consignes de sortie
- déclenchement automatique de changement d'état en fonction d'une grandeur physique mesurée ou après un temps écoulé
- asservissement des sorties par contrôleur `PID <http://en.wikipedia.org/wiki/PID_controller>`_ logiciel