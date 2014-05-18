AngularJS et Python
###################

:date: 2014-05-02 10:12
:tags: python, javascript, AngularJS, Bottle, BeagleBone Black
:author: Nico
:category: Programmation


J'ai commencé il y a quelques jours le `développement d'un outil <https://github.com/njouanin/BBB_admin>`_ qui permettra à terme de visualiser la configuration des ports d'un BeagleBone Black. Réalisé en Python, il utilise différentes commandes systèmes (``uname``, ``ifconfig``, etc.) ainsi que le contenu de l'arobrescence ``sysfs`` pour collecter la configuration système et matérielle de la carte. En particulier il pourra fournir la configuration précise de chacun des ports d'extension du BeagleBone Black. Pour la présentation, les informations collectées seront visualisables via une interface Web réalisée avec `AngluarJS <https://angularjs.org/>`_. Ce post décrit l'architecture retenue pour intégrer Python côté serveur, et `AngluarJS <https://angularjs.org/>`_ côté client.

Présentation d'AngularJS
========================

C'est peut-être un a priori, mais les technos Javascript m'ont toujours rebutées. Néanmoins AngularJs semble bénéficier d'une bonne critique et ses fonctionnalités me semble convenir à mes besoins.

AngularJS est un `framework javascript <https://docs.angularjs.org/guide/introduction>`_ qui permet de construire des applications web dynamiques entièrement côté client. En gros, contrairement aux technos web classiques où c'est le serveur qui génère dynamiquement la page retournée au client, ici c'est le navigateur qui fait le boulot. AngularJS fournit un langage de template, une extension de la syntaxe HTML et une architecture MVC qui permet d'effectuer ce travail côté client. Le serveur se trouve donc allégé de ce travail ce qui est plutôt une bonne chose lorsque l'on souhaite faire héberger une application sur un système embarqué.

Le `tutoriel <https://docs.angularjs.org/tutorial>`_ présent sur le site du projet permet de se faire une idée rapide du fonctionnement d'AngularJS et de ses possibilités. J'espère pouvoir écrire quelques articles prochainement à propos de ce framework.

Python et Bottle coté serveur
=============================

Avec AngularJS, la génération dynamique des pages se passe entièrement côté client, sur le navigateur. Côté serveur un simple serveur HTTP suffit donc pour servir les fichiers statiques qui seront fournis aux clients. Toutefois, il y a toujours une part de dynamique côté serveur afin par exemple de récupérer les données depuis une base de données et qui serviront à l'affichage dynamique sur le client. En pratique on utilisera toujours une technos adaptée à cette situation (Django, PHP, etc.). La différence avec un framework comme AngularJS est que l'aspect dynamique côté serveur n'est utilisé que pour traiter ces données et en fournir aux clients une représentation structurée (type `JSON <http://fr.wikipedia.org/wiki/JSON>`_). Il n'est ainsi plus nécessaire de déployer un `moteur de template <http://en.wikipedia.org/wiki/Web_template_system>`_.

Pour l'outil que je développe (`BBB_admin <https://github.com/njouanin/BBB_admin>`_), l'aspect dynamique sur le serveur est nécessaire pour collecter les informations systèmes et matérielles de la carte. Ces informations seront transmises au client au format JSON et utilisées par AngularJS pour générer les pages et y placer ces données. Pour cela rien de mieux que du Python et un framework Web, `Bottle <http://bottlepy.org/docs/dev/index.html>`_ en l'occurence.

L'architecture de l'outil BBB_admin, repose sur le framework Web `Bottle <http://bottlepy.org/docs/dev/index.html>`_ auquel sont confiés 2 rôles principaux :

* Servir les ressources statiques qui constituent l'interface cliente ;
* Exposer une API JSON permettant au code AngularJS de récupérer les informations du système et du matériel.

On retrouve ces deux fonctionnalités dans l'arborescence du projet :

.. code-block:: bash

  BBB_admin/
    ng-app/
      js/
        app.js
        controllers.js
      partials/
        system.html
      index.html
    static/
      css/
      fonts/
      js/
    api.py
    main.py

Les ressources statiques sont réparties dans les répertoires :

* ``static`` qui contient l'ensemble des ressources statiques de l'interface : fichiers CSS bootstrap, javascript JQuery, images, etc. 
* ``ng-app`` qui contient les scripts spécifiques à AngularJS (la configuration de l'application, les controleurs, etc.), les `vues partielles <https://docs.angularjs.org/tutorial/step_07>`_ et la seule et unique page HTML que contient le site.

L'API JSON est implémentée sous la forme d'une `application Bottle <http://bottlepy.org/docs/dev/api.html#the-bottle-class>`_ dans le fichier `api.py <https://github.com/njouanin/BBB_admin/blob/master/BBB_admin/api.py>`_. Cette application `est montée <https://github.com/njouanin/BBB_admin/blob/master/BBB_admin/main.py#L23>`_ au démarrage.

Conclusion
==========

L'outil BBB_admin est actuellement en cours de dévelopement et j'expérimente encore pas mal de choses avec AngularJS. Toutefois l'architecture retenue me semble cohérente avec une bonne séparations des tâches entre client et serveur. Elle permet également de limiter les ressources nécessaires à son fonctionnement.
