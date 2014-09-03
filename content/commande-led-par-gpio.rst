Commande de LED par GPIO
########################

:date: 2014-03-11 17:15
:tags: électronique, BeagleBone Black, GPIO, BoneScript
:author: Nico
:category: Beaglebone Black
:use_math: true
:figure: /images/commande_led figure.png

Aujourd'hui, je profite de ma présence à `OpenAtelier <http://openatelier.pingbase.net/>`_ pour me faire la main sur la carte Beaglebone Black et commencer à expérimenter quelques montages.

Pour ce premier article, l'objectif *très* simple consiste à commander et faire clignoter une LED connectée à un port GPIO de la carte Beaglebone Black. Le montage réalisée est le suivant :

.. thumbnail:: /images/commande_led_thumb.png
   :alt: Carte Beaglebone Black
   :align: center
   :target: /images/commande_led.png
   :width: 100
   :height: 100
   :scale: 25%
   :class: gallery

Ce montage est simplement constitué d'une LED cablée en série avec une résistance de 220 ohm. La valeur de la résistance est calculée de manière à rester sous la limite de 6mA préconisé sur `la fiche du processeur <http://www.ti.com/lit/ds/symlink/am3359.pdf>`_ (colonne *Buffer strength* du tableau 2-7). 
Etant donné que le port GPIO fournissant une tension de 3,3V et une chute de tension 2,2V aux bornes de la LED, la résistance permet de limiter à 5mA le courant tranversant la LED:

.. math::

 I_{led}=\frac{(V_{gpio}-V_{led})}{R}=\frac{(3,3-2,2)}{220}=5mA 

Le principe de ce montage consiste à commander l'état (0 ou 1) du port GPIO pour alimenter ou non la LED et donc l'allumer ou l'éteindre. Sur ce montage, le port GPIO choisi est le port nommé ``GPIO1_28`` et qui correspond à la patte 12 du connecteur P9. Pourquoi ce port en particulier alors qu'il en existe tant d'autres ? ... tout simplement car par défaut ce port n'est pas utilisé et peut donc être utilisé comme GPIO sans paramétrage spécifique.

Pour ce premier essai, j'ai utilisé la librairie `BoneScript <http://beagleboard.org/Support/BoneScript>`_ qui permet de d'accéder facilement au matériel du Beaglebone Black via le langage Javascript. L'IDE Cloud9 `installé par défaut sur le système Beaglebone Black <http://192.168.7.2:3000>`_ intègre cette librairie. Voici le programme réalisé :

.. raw:: html

 <script src="https://gist.github.com/njouanin/d5724b9b47e7b8b9f214.js"></script>

Le script commence (ligne 2) par importer les fonctionnalités de la librairie BoneScript. Les lignes 4 à 7 permettent d'obtenir une référence sur la patte P9_12 (sur laquelle est connectée la LED) et de la configurer en mode sortie (``b.OUTPUT``). L'état de la LED est contrôlé par la méthode ``toggle``, appelée toutes les toutes les 500 milli-secondes. La méthode change alternativement l'état du port (``LOW`` ou ``HIGH``) sur la patte ce qui a pour effet de faire clignoter la LED.

Pour finir, j'ai voulu testé le même script en ligne de commande en accédant directement au port GPIO via le noyau Linux. Voici le script réalisé :

.. raw:: html

 <script src="https://gist.github.com/njouanin/58648d33fed27e8dd4ac.js"></script>

Le script commence par réserver (ligne 2) un accès au port ``GPIO1_28``. La valeur 60 est calculée à partir de l'emplacement du port par la formule suivante :

.. math::

 port=32*n + p

Les valeurs de :math:`n` et :math:`p` sont déterminés à partir du nom du port, par la notation : GPIO **n** _ **p** . Pour accéder au port ``GPIO1_28`` il convient donc d'écrire la valeur :math:`32*1+28=60` dans le fichier ``export``. 

La ligne 4 a ensuite pour objectif de configurer le port en sortie. Enfin le script ligne 5, écrit alternativement les valeurs 0 ou 1 dans le fichier ``value`` ce qui a pour effet de changer l'état du port et donc d'allumer ou éteindre la LED.
