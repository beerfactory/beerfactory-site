Alimentation d'une LED connectée à un port GPIO
###############################################

:date: 2014-04-11 21:26
:tags: électronique, BeagleBone Black, GPIO
:author: Nico
:category: Beaglebone Black
:use_math: true
:figure: /images/alim_led_img2_figure.png

Comme j'ai eu l'occasion de l'illustrer dans `cet article <{filename}/commande-led-par-gpio.rst>`_, le moyen le plus simple pour allumer une LED à partir d'un port GPIO du BeagleBone Black consiste à l'alimenter directement par la tension de sortie du port (3,3V). Toutefois, une résistance doit absolument être placée en série afin de limiter le courant traversant la LED à 6mA. Cette limite correspond à l'intensité maximale que peut fournir le processeur d'après `la fiche du constructeur <http://www.ti.com/lit/ds/symlink/am3359.pdf>`_. Voici ce montage extrèmement simple ...

.. thumbnail:: /images/alim_led_img1_thumb.png
   :target: /images/alim_led_img1.png
   :align: center
   :scale: 50%
   :class: gallery
   :alt: Alimentation LED


Le port GPIO du BeagleBone Black fournit une tension de sortie de 3,3V. Etant donnée une chute de tension de 2V aux bornes de la LED, le courant :math:`I_{led}` circulant dans ce circuit vaut bien :math:`6mA`.

.. math::

 I_{led}=\frac{(V_{gpio}-V_{led})}{R}=\frac{(3,3-2)}{220}=6mA 

Ce montage fonctionne donc aux limites du processeur avec pour inconvénient supplémentaire une faible luminosité de la LED. Sachant qu'une LED classique atteind son rendement lumineux entre 15mA et 20mA, il est clair que ce montage n'est pas adapté si l'on souhaite disposer d'un éclairage maximal. 

Montage à transistor
====================

Pour être sûr de rester dans les limites du processeur tout en disposant d'une luminosité maximale, la solution consiste à intercaler un transistor `BC547 <http://pdf.datasheetcatalog.net/datasheet/fairchild/BC547.pdf>`_ utilisé en commutation, soit ce nouveau schéma :

.. thumbnail:: /images/alim_led_img2_thumb.png
   :target: /images/alim_led_img2.png
   :align: center
   :scale: 50%
   :class: gallery
   :alt: Alimentation LED

Le raisonnement suivant est utilisé pour calculer les résistances R1 et R2 (les valeurs utilisées dans les calculs suivants sont extraites de la `datasheet du transistor BC547 <http://pdf.datasheetcatalog.net/datasheet/fairchild/BC547.pdf>`_).

Calcul de R1
------------

:math:`R_1` est calculée de manière à limiter le courant :math:`I_c` circulant dans la LED à 20mA lorsque le transistor :math:`T_1` est saturé, soit :

.. math::

 R_1\geq\frac{5-V_{led}-V_{cesat}}{I_c} = \frac{5-2-1}{20.10^-3} = 100 \Omega

En valeur normalisée on pourra prendre :math:`R_1=100 \Omega` ou de préférence :math:`R_1=120 \Omega` pour évider d'être aux limites de la LED. Dans ce cas le courant :math:`I_c` réel sera vaudra 16mA.

Calcul de R2
------------

Pour que la LED s'allume lorsque l'état du port GPIO passe à 1, il faut rendre le transistor passant. C'est le cas sur le schéma proposé : lorsque le port GPIO passe à 1 (3,3V), la tension :math:`V_{be} = V_{besat}` et le transistor est donc passant. 

:math:`R_2` est présente pour limiter le courant de base :math:`I_b` et ne pas déteriorer le transistor. Toutefois, le courant :math:`I_b` doit être supérieur à :math:`\frac{I_C}{\beta}` pour que le transistor soit saturé. On a donc dans le cas le plus défavorable (:math:`\beta_{min}=100`):

.. math::

 R_2\leq\frac{V_{gpio}-V_{besat}}{I_c}\times\beta = \frac{3,3-0,7}{16.10^-3}\times 100 = 16250\Omega

Soit :math:`R_2=15k\Omega` en valeur normalisée.

Conclusion
==========

Le schéma proposé permet de respecter les spécifications d'utilisation du processeur et donc de garantir son fonctionnement à long terme. Les valeurs des résistances :math:`R_1` et :math:`R_2` peuvent être ajustées en fonction de la luminosité souhaitée. Leur valeur dépend également des caractéristiques du transistor utilisé.

Ce schéma peut également être généralisé et utilisé pour alimenter d'autres types d'éléments (relais, moteurs, etc.). Dans ce cas il faudra évidemment revoir le choix et le dimensionnement des composants en fonction des tensions d'alimentation et de la puissance dissipée.

Enfin, pour une mise en oeuvre de ce schéma sur la carte BeagleBone Black, la tension d'alimentation 5V pourra être prise sur la patte ``VDD_5V`` du connecteur P9.

Références
==========

`<http://wiki.mdl29.net/doku.php?id=elec:quelques_rappels_theoriques#transistors>`_

`<http://xizard.chez.com/Cours/transistor_commutation.htm>`_