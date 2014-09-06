Découverte du Beaglebone Black
##############################

:date: 2014-03-08 22:11
:tags: électronique, linux, embarqué, BeagleBone Black
:author: Nico
:category: Beaglebone Black
:figure: /images/product_detail_black_lg_figure.jpg

Arrivée sur le marché en avril 2013, la carte Beaglebone Black se positionne en concurrent du `Raspberry Pi`_ avec des caractéristiques techniques identiques ou légèrement supérieures. Processeur `ARM Cortex-A8`_ à 1GHz, 512Mo de RAM, 2Go de flash eMMC, ports à foison le tout construit dans un esprit open-source et à un prix abordable (47€ chez `Lextronic <http://www.lextronic.fr/P28675-platine-beaglebone-black-rev-a6a.html>`_). 

.. image:: /images/product_detail_black_lg.jpg
   :alt: Carte Beaglebone Black
   :align: center

Pour le projet `Lulu la nantaise <{filename}pages/lulu-la-nantaise.rst>`_ je suis à la recherche d'une carte capable de servir d'interface avec les capteurs et les actionneurs de la pico-brasserie, mais également d'héberger la partie logicielle assurant le suivi et le pilotage de la pico-brasserie. Dès lors la carte Beaglebone Black apparaît comme un bon candidat; j'ai donc fait l'acquisition d'un exemplaire afin détudier ses possibilités et commencer la mise en oeuvre du projet. 

J'inaugure donc une série d'articles autour de la carte Beaglebone Black, sa prise en main et son utilisation dans le cadre d'un projet embarqué. 


Caractéristiques techniques
===========================

Physiquement la carte a les dimensions d'une carte de crédit sur laquelle sont disposés les principaux composants et connecteurs :

.. image:: /images/BBB_composants.png
   :alt: Principaux composants de la carte Beaglebone Black
   :align: center
   :width: 80%
   :target: /images/BBB_composants.png

Côté composants, on note l'emplacement des composants suivants :

* Mémoire DDR3 512Mo ;
* Le `contrôleur d'alimentation <http://en.wikipedia.org/wiki/Power_management_IC>`_ (`TPS65217C <http://www.ti.com/product/tps65217c>`_) chargé d'alimenter les éléments en 3,3V ou 5V en fonction des sources d'alimentation;
* Le contrôleur Ethernet;
* La `mémoire Flash <http://fr.wikipedia.org/wiki/M%C3%A9moire_flash>`_ 2Go;
* Le contrôleur HDMI;
* et évidemment le processeur `ARM <http://fr.wikipedia.org/wiki/Architecture_ARM>`_ en position centrale;

.. image:: /images/BBB_connecteurs.png
   :alt: Principaux connecteurs de la carte Beaglebone Black
   :align: center
   :width: 80%
   :target: /images/BBB_connecteurs.png

Côté composants on trouve :

* Un port USB "Host" permettant la connexion de périphériques USB (clavier, souris, etc.);
* Un connecteur écran `microHDMI <http://fr.wikipedia.org/wiki/High-Definition_Multimedia_Interface#Types_de_connecteurs>`_;
* Un connecteur `microSD <http://fr.wikipedia.org/wiki/MicroSD>`_;
* Un port USB "Client" permettant de relier la carte à un ordinateur "maître";
* Un port Ethernet 10/100;
* Un connecteur d'alimentation (d'utilisation optionnelle, la carte pouvant être alimentée par le port USB ou par les connecteurs d'extention);
* Deux connecteurs latéraux d'extensions dits P8 et P9 par lesquels l'ensemble des ports d'extensions sont accessibles (et dont nous reparlerons plus tard ...);

Concernant les caractéristiques techniques de la chose, voilà les informations que l'on peut trouver dans le `manuel de référence (SRM en anglais) <https://github.com/CircuitCo/BeagleBone-Black/blob/master/BBB_SRM.pdf?raw=true>`_ :

.. image:: /images/BBB_features.png
   :alt: Caractéristiques techniques Beaglebone Black
   :align: center

Passsons sur la puissance du processeur, la quantité mémoire, où les capacités graphiques. Tout est relatif dans ce domaine et fonction de l'utilisation que l'on en fait. Il est par contre plus intéressant de s'attarder sur le nombre et la diversité des extensions disponibles et notamment :

* 5 ports séries (+ 1 port de débogage);
* 2 bus séries `SPI <http://fr.wikipedia.org/wiki/Serial_Peripheral_Interface>`_;
* 3 bus `I2C <http://fr.wikipedia.org/wiki/I2C>`_;
* 69 entrées/sorties génériques programmables (`GPIO <http://fr.wikipedia.org/wiki/GPIO>`_)
* 4 convertisseurs analogiques-numériques 12 bits.
* 7 timers

L'ensemble de ces ports sont accessibles via les connecteurs P8 et P9. Il faut par contre savoir que tous les ports ne sont pas accessibles directement. En effet, chacun de ces ports correspondent à des pattes du microprocesseur et afin d'en limiter leur nombre celui-ci a recours à un mécanisme de multiplexage de ports. 

Pour faire simple, chaque patte du microprocesseur (et donc des connecteurs P8 et P9) peut avoir plusieurs fonctions (jusqu'à 8). Les tableaux 12 et 13 du `manuel de référence <https://github.com/CircuitCo/BeagleBone-Black/blob/master/BBB_SRM.pdf?raw=true>`_ décrivent les configurations possibles. A titre d'exemple, la patte 26 du connecteur P9 peut avoir pour fonction :

* Port RX de l'UART 1 (mode 0);
* Port SDA du bus I2C 1 (mode 3);
* Port générique d'entrée/sortie GPIO14 (mode 7);

Ces fonctions sont exclusives et peuvent être configurées par logiciel. 

Premier démarrage et prise en main
==================================

La carte Beaglebone est disponible à la vente en ligne sur différents sites spécialisées. J'ai acheté la mienne sur le site de `Lextronic <http://www.lextronic.fr/P28675-platine-beaglebone-black-rev-a6a.html>`_ pour 55€, frais de ports inclus. 

La carte est livrée dans un emballage carton, simplement accompagnée d'un cable USB et de quelques instructions de démarrage. 

.. image:: /images/BBB_deballage_mini.jpg
   :alt: Contenu de la livraison
   :align: center
   :target: /images/BBB_deballage.jpg

Pour démarrer, il suffit de la raccorder à un ordinateur (PC/MAC/Linux) via le port USB client. Après quelques instants, la carte est montée et apparaît comme une carte USB sur le système. 

.. raw:: html

  <iframe width="560" height="315" src="//www.youtube.com/embed/sRNei7t-W48" frameborder="0" allowfullscreen></iframe>)


Sur Windows et Mac, des drivers doivent être installés afin de rendre la carte accessible via un réseau virtuel sur le port USB. La carte est alors configurée avec l'adresse 19.168.7.2 et elle répond sur le `port HTTP <http://192.168.7.2>`_ ou via SSH (login ``root`` sans mot de passe). Il est également possible d'accéder à `Cloud9 <https://c9.io/>`_ à l'adresse `http://192.168.7.2:3000 <http://192.168.7.2:3000>`_ pour accéder à l'IDE permettant de coder en BoneScript. 

Victime de son succès ?
------------------------

La carte Beaglebone Black semble être victime de son succès car elle est régulièrement indiquée indisponible sur `Lextronic <http://www.lextronic.fr/P28675-platine-beaglebone-black-rev-a6a.html>`_ et les autres sites tels que `Conrad <http://www.conrad.fr/ce/fr/product/409907/Carte-Mini-PC-BeagleBone-Black-BeagleBoard-BB-BBLK-000?ref=searchDetail>`_ ou `RS <http://radiospares-fr.rs-online.com/web/p/kits-de-developpement-pour-processeurs-et-microcontroleurs/7753805/>`_. J'ai pu commander la mienne début février après une première rupture de stock. Elle semble de nouveau indisponible début mars.



.. _ARM Cortex-A8 : http://fr.wikipedia.org/wiki/ARM_Cortex-A8
.. _Raspberry Pi: http://www.raspberrypi.org/