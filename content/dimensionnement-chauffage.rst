Dimensionnement des éléments de chauffage
##########################################

:date: 2014-02-05 16:15
:tags: pico, électricité, mathplotlib, puissance, thermique
:author: Nico
:category: Pico
:use_math: true

Le dimensionnement des éléments de la pico-brasserie lulu la nantaise est un préalable essentiel à sa construction. L'objectif est de déterminer les caractéristiques des éléments principaux qui permettront de répondre au cahier des charges, notamment la capacité de brassage désirée. 

Dans cette phase de dimensionnement, le choix des éléments de chauffage est délicat. Pour une pico-brasserie électrique il s'agit de déterminer les caractéristiques des éléments chauffants qui assureront la montée en température du moût pendant le brassage et l'ébullition. Ces éléments doivent être correctment dimensionnés afin de répondre à 3 contraintes principales :

* être adapté au chauffage de liquide jusqu'à des températures de 100°c;
* assurer une montée rapide de la température;
* limiter les risques de caramélisation du moût (sucré) au contact de l'élément chauffant;

La satisfation de ces contraintes est satisfaite par le calcul d'une puissance adéquate des résistances chauffantes. En théorie, plus la puissance est importante plus le chauffage sera efficace et rapide. En pratique le choix de la puissance devra tenir compte des capacités limitées de l'installation électrique. 

Ainsi le calcul de la puissance de chauffage disponible est primordial puisque c'est cette puissance qui déterminera directement la capacité de brassage et donc le dimensionnement des autres éléments de la brasserie. Les paragraphes suivants exposent le calcul réalisé dans le cas de la pico-brasserie lulu la nantaise.

Un peu de théorie
=================

Le chauffage, ou l'élévation de température, d'un corps se produit au contact ou au voisinage d'un autre corps de température plus élevée. Il se produit alors un transfert d'énergie, le `transfert thermique`_, du corps le plus chaud vers le plus froid jusqu'à équilibre de la température des deux corps.

Dans ces conditions, la quantité d'énergie nécessaire pour élever la température d'un corps de masse :math:`m` de la température :math:`t_1` à la température :math:`t_2` dépend de sa `capacité thermique massique`_ :math:`C_m`. Cette quantité d'énergie :math:`Q` est calculée par la formule suivante :

.. math::

 \Delta_\theta=(t_2-t_1)

 Q = m.C_m.\Delta_\theta

avec :

* :math:`Q` l'énergie nécessaire exprimée en Joules (J)
* :math:`m` exprimée en grammes (g)
* :math:`\Delta_\theta` exprimée en Kelvin (K)

 **Application**

 La capacité thermique massique de l'eau à l'état liquide étaestnt de :math:`4,185 J.g^{-1}.K^{-1}`. Ainsi, la quantité d'énergie nécessaire pour augmenter la température de :math:`1kg` d'eau de :math:`1K` est égale à :

 .. math::
  Q = 1000g\times4,185\times1K = 4185 J

La `puissance thermique`_, ou puissance de chauffage, désigne la *quantité d'énergie* qu'un système fourni par unité de temps. Dans le `système international d'unités`_ cette puissance s'exprime en watts (:math:`W`) et correspond à la quantité d'énergie qu'un système produit en 1 seconde :

.. math::

 1 W = 1 J.s^{-1}


Ainsi, un système dont la puissance est de 1000 watts produit une énergie de 1000 joules par seconde. Un tel système sera donc capable d'augmenter la température de :math:`1kg` d'eau en :

.. math::

 t = \frac{4185 J}{1000 W} = 4,185 s

Pour les TP, essayez avec une bouilloire !

 **Application**

 Etant donné un volume d'eau de :math:`20l` à la température initiale de :math:`15^\circ c`, quelle est la puissance de chauffage nécessaire pour porter ce volume à ébullition (:math:`100^\circ c`) en 30 minutes (et en considérant que pour l'eau :math:`1l = 1kg`.)?

 Réponse :

  * L'énergie nécessaire pour amener les :math:`20l` d'eau à ébullition est égale à :

  .. math::
   Q = 20000g\times4,185\times (100-15) = 7114500J

  * Pour produire cette énergie en 30 minutes il faut disposer d'un système capable de fournir une puissance de chauffage égale à :

  .. math::

   P = \frac{7114500}{30\times60} = 3952 W

.. links
.. _puissance thermique: http://fr.wikipedia.org/wiki/Puissance_(physique)#Puissance_thermique
.. _système international d'unités: http://fr.wikipedia.org/wiki/Syst%C3%A8me_international_d%27unit%C3%A9s
.. _transfert thermique: http://fr.wikipedia.org/wiki/Transfert_thermique
.. _capacité thermique massique: http://fr.wikipedia.org/wiki/Capacit%C3%A9_thermique_massique


En pratique
===========

En théorie, une puissance de 1W suffit à chauffer toute quantité d'eau jusqu'à 100°c, ce n'est qu'une question de temps... En pratique ce n'est pas possible car il faut prendre en compte les pertes dues à l'environnement et notamment l'efficacité d'isolation du système. 

En appliquant les formules décrites précédemment on peut déterminer la puissance de chauffage nécessaire, en théorie, pour le fonctionnement de la pico-brasserie. Il s'agit de déterminer la puissance nécessaire pour porter le moût à ébullition (:math:`1^\circ c`) en un temps raisonnable. La limite de l'installation électrique déterminera la puissance maximale disponible et donc le volume maximale qu'il sera possible de chauffer jusqu'à 100°c. 

Concrètement, le temps nécessaire élever la température d'une masse d'eau :math:`m` de :math:`1^\circ c` est fonction de la massage à chauffer et de la puissance de chauffage d'après la relation suivante :

.. math::

 t = \frac{m\times4,185\times1^\circ c}{P}

avec :

* :math:`m` la masse d'eau exprimée en grammes (g)
* :math:`P` La puissance de chauffage en watt (W)

Cette relation est tracée sur le diagramme suivant pour des volumes d'eau de 20l, 50l, 70l et 100l. En se basant sur un rythme de montée en température de :math:`1^\circ c` par minute, ce diagramme met également en évidence les puissances de chauffe nécessaire.

.. image:: /images/temp_fct_puissance.png
   :alt: Temps nécessaire pour élever la température d'une masse d'eau de 1°C en fonction de la puissance de chauffe
   :align: center

Ces puissances permettent de déterminer la capacité maximale de brassage en se basant sur la limite de l'installation électrique. En France, classiquement, les abonnements électriques 6kVA correspondent à une limite de 30A. Dans cette configuration la puissance maximale instantanée est limitée à :

.. math::
 
 230 V \times 30 A = 6900W

En général les éléments de chauffe sont alimentés en courant alternatif 230V, l'intensité fournie aux éléments de chauffe ne devra donc pas dépasser 30A. Il faut également prévoir une marge pour alimenter le reste de la pico-brasserie et le reste du domicile pendant le brassage. Le tableau suivant présente un résumé des différentes options possibles :

==================== ==================== ====================
Capacité de brassage Puissance nécessaire Intensité sous 230 V
==================== ==================== ====================
20 l                 1395 W               6,06 A
50 l                 3487 W               15,1 A
70 l                 4882 W               21,2 A
100 l                6975 W               30,3 A
==================== ==================== ====================


On voit clairement que la capacité de 100l est incompatible avec une installation électrique domestique. **La capacité de 70l semble est le maximum qui permette de brasser dans des temps raisonnable**. Elle laisse une marge de 2000 W pour les besoins de l'installation pendant le brassage.

La pico-brasserie Lulu la nantaise sera dimensionnée sur cette base, soit une capacité de brassage maximale de 70l.
