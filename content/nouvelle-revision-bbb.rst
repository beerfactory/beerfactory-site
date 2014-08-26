Nouvelle révision de la carte BeagleBone Black
==============================================

:date: 2014-05-20 22:41
:tags: BeagleBone Black, Debian, Linux
:author: Nico
:category: Beaglebone Black

La communauté Beagleboard `a annoncé <http://www.beagleboard.org/blog/2014-05-14-have-no-fear-revc-is-here/>`_ la disponibilité d'une nouvelle révision de la carte BeaglaBone Black. Nommé revision ``C``, elle apporte principalement :

* le passage de 2Go à 4Go de l'espace de stockage disponible sur la carte. Ce choix répond aux besoins des utilisateurs et rend la carte plus viable à long terme. Par contre une légère augmentation de prix (de l'ordre de $15) est à prévoir;
* le passage du système d'exploitation sous `Debian <http://beagleboard.org/project/debian/>`_;

Concernant le passage sous Debian, cette distribution n'est pas réservée à la révision C, elle est installable sur les anciennes révisions ainsi que sur les autres cartes produites par BeagleBoard. 

J'espère pouvoir tenter cette migration bientôt et faire un retour sur ce blog.

**Mise à jour le 21/05** : Ca y est c'est fait ! Copie de `l'image <http://beagleboard.org/latest-images>`_ sur une carte SD, redémarrage du système (en appuyant sur le bouton dédié), 30 minutes de patience le temps de flasher la mémoire, et hop, la carte redémarre sur debian :

.. code-block:: bash

  root@beaglebone:~# cat /etc/debian_version
  7.5