Commande de LED par GPIO
########################

:date: 2014-03-11 17:15
:tags: électronique, BBB, GPIO, BoneScript
:author: Nico
:category: Beaglebone Black
:Status: draft

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

Ce montage est simplement constitué d'une LED cablée en série avec une résistance de 220 ohm. Le port GPIO fournissant une tension de 3,3V, la résistance permet de limiter à 15mA le courant tranversant la LED.

Le principe de ce montage consiste à commander l'état (0 ou 1) du port GPIO pour alimenter ou non la LED et donc l'allumer ou l'éteindre. Sur ce montage, le port GPIO choisi est le port nommé ``P8_13`` et qui correspond à la patte 13 du connecteur P8. Pourquoi ce port en particulier alors qu'il en existe tant d'autres ? ... 

Pour ce premier essai, j'ai utilisé la librairie `BoneScript <http://beagleboard.org/Support/BoneScript>`_ qui permet de d'accéder facilement au matériel du Beaglebone Black via le langage Javascript. L'IDE Cloud9 `installé par défaut sur le système Beaglebone Black <http://192.168.7.2:3000>`_ intègre cette librairie. Voici le programme réalisé :

.. code-block:: javascript
   :linenos:

   /*Clignotement de la led connectée sur le port P8_13*/
   var b = require('bonescript');

   var pins = b.bone.pins;
   var ledPin = pins.P8_13;

   b.pinMode(ledPin, b.OUTPUT);

   var state = b.LOW;
   b.digitalWrite(ledPin, state);
 
   setInterval(toggle, 500);
 
   function toggle() {
     if(state == b.LOW) state = b.HIGH;
     else state = b.LOW;
     b.digitalWrite(ledPin, state);
   }

Le script commence (ligne 2) par importer les fonctionnalités de la librairie BoneScript. Les lignes 4 à 7 permettent d'obtenir une référence sur la patte P8_13 (sur laquelle est connectée la LED) et de la configurer en mode sortie (``b.OUTPUT``). L'état de la LED est contrôlé par la méthode ``toggle``, appelée toutes les toutes les 500 milli-secondes. La méthode change alternativement l'état du port (``LOW`` ou ``HIGH``) sur la patte ce qui a pour effet de faire clignoter la LED.
