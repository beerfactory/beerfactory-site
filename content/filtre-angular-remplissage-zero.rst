Filtre AngularJS de remplissage par des 0
=========================================

:date: 2014-05-18 12:13
:tags: javascript, AngularJS
:author: Nico
:category: Programmation

Tout est dans le titre, enfin presque...

Il s'agit dans cet article de faire connaissance avec les `filtres AngularJS <https://docs.angularjs.org/guide/filter>`_ et de réaliser pour cela un filtre qui remplit un champs par des ``0`` à gauche sur une longueur donnée. Par exemple étant donné un champs de longueur ``4`` (caractères) et la donnée à afficher ``12``, le filtre doit permettre d'afficher ``0012``.

J'ai déposé le code de ce filtre et un exemple d'utilisation sur `JSFiddle <http://jsfiddle.net/gh/gist/angularjs/1.2.1/3348ed708d527de8641c/>`_. Le coeur du filtre correspond au code suivant :

.. code-block:: javascript

  return function(input, n) {
    if(input === undefined)
      input = ""
    if(input.length >= n)
      return input
    var zeros = "0".repeat(n);
    return (zeros + input).slice(-1 * n)
  };

Le paramètre ``input`` contient le texte passé au filtre par Angular, c'est-à-dire le contenu de ce qu'il y a avant le ``|``. Le paramètre ``n`` correspond au paramètre passé en argument du filtre, ``4`` dans cet exemple.

Le code du filtre, après les vérifications de forme, initialise une chaine composée uniquement de ``0`` sur une longueur de ``n`` caractères. Le texte en entrée est concaténé avec cette chaine, et uniquement les ``n`` derniers caractères (``slice(-1 * n)``) sont retournées. On arrive ainsi au résultat souhaité.

Pour être utilisé, ce filtre doit être déclaré dans l'application AngularJS en déclarant un nouveau module (ici ``filters``) et en y déclarant un nouveau filtre par appel de la méthode ``filter()``. Cette méthode prend en argument le nom du filtre à ajouter (ici ``zpad``) et la méthode à appeler, telle que vue précédemment. Il faut également penser à ajouter ce nouveau module en tant que dépendance de l'application ``MyApp`` :

.. code-block:: javascript

  angular.module('MyApp', ['filters']);

  angular.module('filters', []).filter('zpad', function() {
	return function(input, n) {
		if(input === undefined)
			input = ""
		if(input.length >= n)
			return input
		var zeros = "0".repeat(n);
		return (zeros + input).slice(-1 * n)
	};
  });

Enfin, dans le code HTML, le filtre s'utilise simplement de la manière suivante :

.. code-block :: html

  <p>{{12 | zpad:4}}</p>

Avec cet exemple, AngularJS affichera ``0012``. La page sur `JSFiddle <http://jsfiddle.net/gh/gist/angularjs/1.2.1/3348ed708d527de8641c/>`_ permet d'expérimenter l'utilisation de ce filtre.

Ce code est également disponible sur `GitHub <https://gist.github.com/njouanin/3348ed708d527de8641c>`_.
