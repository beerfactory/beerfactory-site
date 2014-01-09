Intégration de Yuml dans Sphinx-doc
########################################

:date: 2014-01-09 17:15
:tags: python, sphinx-doc
:author: Nico
:Status: draft

Yuml_ est un outil de génération de diagrammes UML en ligne. Il offre une API simple et un langage de description permettant de générer des sorties PNG, JPG, SWF ou PDF pour des diagrammes de classes, d'activités ou de cas d'utilisation. Il suffit de jeter un oeil à ces `pages d'exemples <http://yuml.me/diagram/scruffy/class/samples>`_ pour avoir une idée des fonctionnalités de Yuml_. Voici un exemple : ::

  [Brewery]<>-*>[Equipment]
  [Equipment]-*>[Sensor]
  [Sensor]-1>[SamplingConfiguration]
  [Sensor]-1>[ConversionConfiguration]

L'envoi à l'API Yuml_ de ce texte renvoie une image contenant le diagramme de classe suivant :

.. image:: /static/images/yuml-class-diagram.png
   :alt: Exemple de diagramme de classes UML
   :align: center

Pour aller plus loin avec Yuml_ je me suis lancé comme défit de pouvoir intégrer l'API Yuml_ dans le générateur de documentation Sphinx_. L'objectif de pouvoir intégrer des descriptions Yuml_ directement dans des documents au format `restructured <https://github.com/beerfactory/brewbox-doc>`_ et d'utiliser le `mécanisme d'extension <http://sphinx-doc.org/extensions.html>` de Sphinx_ pour générer les diagrammes UML à la volée.

Pour cela, je me suis inspiré d'une extension existante pour `Gnuplot <https://bitbucket.org/birkenfeld/sphinx-contrib/src/dc99bd08ef54d09be5be8bf6f7692a7fa310778c/gnuplot/?at=default>`_. Cette nouvelle extensio ne nomme ``sphinxcontrib-yuml``. Elle définit une nouvelle directive ``yuml::`` qui fonctionne comme la directive ``image::`` à la différence qu'aucun fichier source n'est nécessaire. L'image est générée lors de la compilation de la documentation, par appel de l'API Yuml_ *à la volée*.

Plus concrètement, gràce à l'extension ``sphinxcontrib-yuml`` il devient possible d'écrire des directives telles que celle-ci : ::

  .. yuml:: 
	:style: plain 

	[Customer]->[Billing Address]

pour obtenir automatiquement l'image suivante dans une documentation Sphinx_ :

.. image:: /static/images/yuml-class-diagram2.png
   :alt: BrewBox sample UML diagram
   :align: center

The ``sphinxcontrib-yuml`` extension sources are published on `Github <https://github.com/njouanin/sphinxcontrib-yuml>`_. Python package is available on `Pypi <https://pypi.python.org/pypi/sphinxcontrib-yuml>`_. Documentation and configuration options are described in the `README <https://github.com/njouanin/sphinxcontrib-yuml/blob/master/README.rst>`_ file.

.. links
.. _Yuml: http://yuml.me/
.. _Sphinx: http://sphinx-doc.org/
.. _OmniGraffle: http://www.omnigroup.com/omnigraffle
