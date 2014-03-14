Premiers pas avec matplotlib
############################

:date: 2014-02-06 21:06
:tags: mathplotlib, python
:author: Nico
:category: Python

Pour le `dimensionnement des éléments de chauffage <{filename}/dimensionnement-chauffage.rst>`_, j'ai été amené à utiliser `matplotlib`_ pour tracer et analyser la relation existante puissance et temps de chauffage.

En deux mots, `matplotlib`_ est une librairie Python qui permet d'effectuer des tracés et des graphiques en 2D. La `documentation <http://matplotlib.org/contents.html>`_ est riche et offre un `tutorial <http://matplotlib.org/users/pyplot_tutorial.html>`_ qui permet de rentrer rapidement dans le vif du sujet.

Voici le graphique réalisé avec `matplotlib`_ et présent dans l'article sur le `dimensionnement des éléments de chauffage <{filename}/dimensionnement-chauffage.rst>`_

.. image:: /images/temp_fct_puissance.png
   :alt: Graphique matplotlib
   :align: center

Ce graphique a été généré par le script suivant et disponible sur `github <https://github.com/beerfactory/beerfactory-site/blob/master/scripts/plot_temp_fct_puissance.py>`_ :

.. code-block:: python3
   :linenos: table

 import numpy as np
 import matplotlib.pyplot as plt

 r = np.arange(1000.0, 8100.0, 100.0)

 def f(m,t):
	'''Temps nécessaire pour élever la température d''une masse d''eau m de 1°C en fonction de la puissance de chauffe'''
	return ((m*1000.0*4.185)/t)/60.

 plt.plot(r, f(20,r), 'b', label='20 l')
 plt.plot(r, f(50,r), 'g', label='50 l')
 plt.plot(r, f(70,r), 'r', label='70 l')
 plt.plot(r, f(100,r), 'c', label='100 l')
 plt.axhline(y=1,linestyle=':')
 #Intersection 20l
 plt.axvline(x=1395., ymax=0.15, linestyle=':')
 plt.plot(1395.,1., 'o')
 plt.annotate('1395W', xy=(1395., 1.0), xytext=(1595., 1.5),
	arrowprops=dict(facecolor='black', shrink=0.1))
 #Intersection 50l
 plt.axvline(x=3487.5, ymax=0.15, linestyle=':')
 plt.plot(3487.5,1., 'o')
 plt.annotate('3487W', xy=(3487.5, 1.0), xytext=(3687., 1.5),
	arrowprops=dict(facecolor='black', shrink=0.1))
 #Intersection 70l
 plt.axvline(x=4882.5, ymax=0.15, linestyle=':')
 plt.plot(4882.5,1., 'o')
 plt.annotate('4882W', xy=(4882.5, 1.0), xytext=(5082., 1.5),
	arrowprops=dict(facecolor='black', shrink=0.1))
 #Intersection 100l
 plt.axvline(x=6975., ymax=0.15, linestyle=':')
 plt.plot(6975.,1., 'o')
 plt.annotate('6975W', xy=(6975., 1.0), xytext=(7175., 1.5),
	arrowprops=dict(facecolor='black', shrink=0.1))

 plt.xlabel('Puissance (W)')
 plt.ylabel('Temps (min)')
 plt.legend()
 plt.show()

Le script début par les classiques imports de modules, matplotlib et numpy en l'occurence et initialise ensuite un intervalle de valeur. Cet intervalle correspond à l'intervalle de puissances qui sera utilisé en abscices pour tracer les différents graphes. La ligne suivante initialise un intervalle de valeur de 1000 à 8000 watts, par intervalle de 100 W.

.. code:: python

 r = np.arange(1000.0, 8100.0, 100.0)

La fonction à tracer est ensuite déclarée dans la méthode :

.. code:: python

 def f(m,t):
	'''Temps nécessaire pour élever la température d''une masse d''eau m de 1°C en fonction de la puissance de chauffe'''
	return ((m*1000.0*4.185)/t)/60.

Le paramètre ``m`` correspond à la masse d'eau. ``t`` représente la puissance. Les 4 lignes suivantes déclenchent le calcul des ordonnées par appel de la fonction ``f()`` appliquée à l'intervalle de puissances et une masse d'eau fixe. Ces 4 courbes seront tracées sur le même graphe.

.. code:: python

 plt.plot(r, f(20,r), 'b', label='20 l')
 plt.plot(r, f(50,r), 'g', label='50 l')
 plt.plot(r, f(70,r), 'r', label='70 l')
 plt.plot(r, f(100,r), 'c', label='100 l')

La suite du script permet de tracer :

* une ligne horizontale en ordonnée ``1.0`` :

.. code:: python

 plt.axhline(y=1,linestyle=':')

* une ligne vertical à l'intersection de la ligne horizontale et de chacune des courbes. L'intersection est matérialisée par un point et un texte précisant la valeur de l'intersection en abscice :

.. code:: python

 #Intersection 20l
 plt.axvline(x=1395., ymax=0.15, linestyle=':')
 plt.plot(1395.,1., 'o')
 plt.annotate('1395W', xy=(1395., 1.0), xytext=(1595., 1.5),
	arrowprops=dict(facecolor='black', shrink=0.1))

* les légendes sur les axes et le graphique :

.. code:: python

 plt.xlabel('Puissance (W)')
 plt.ylabel('Temps (min)')
 plt.legend()

Enfin le script affiche le graphe généré :

.. code:: python

 plt.show()

Le graphe peut également être enregistré directement :

.. code:: python

 plt.savefig("../content/images/temp_fct_puissance.png")



.. links
.. _matplotlib: http://matplotlib.org/

