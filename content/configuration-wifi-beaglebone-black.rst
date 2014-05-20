Configuration de la connexion Wifi sur BeagleBone Black
=======================================================

:date: 2014-05-18 12:13
:tags: wifi, BeagleBone Black, 
:author: Nico
:category: Beaglebone Black
:Status: draft

La carte BeagleBone black n'intègre pas d'interface réseau Wifi (c'est dommage ...) et il est nécessaire d'utiliser un adaptateur Wifi USB pour la connecter un réseau sans-fil. Cet artcile décrit la procédure à suivre pour installer et configurer un tel adaptateur. Cette procédure est largement inspiré de `ce tutorial Adafruit <https://learn.adafruit.com/beaglebone/wifi>`_ et en fournit donc une traduction

Choix de l'adaptateur Wifi
--------------------------

Choix crucial, puisqu'il s'agit de choisir l'adaptateur qui soit le mieux supporté par la carte et le système. La page wiki de la carte BeagleBone Black propose une `liste d'adaptateurs compatibles <http://www.elinux.org/Beagleboard:BeagleBoneBlack#WIFI_Adapters>`_. Pour ma part, j'ai opté pour l'adaptateur `Dlink DWA-121 <http://www.dlink.com/fr/fr/home-solutions/connect/adapters/dwa-121-wireless-n-150-pico-usb-adapter>`_ qui offre la compatibilité Linux la plus large pour un prix dérisoire (9,90€ chez `Amazon <http://www.amazon.fr/D-Link-DWA-121-Pico-WiFi-N150/dp/B004X8R7HY>`_).

.. image:: /images/DWA121.jpg
   :alt: Adaptateur Wifi USB Dlink DWA-121
   :align: center

Pré-requis
----------

La première opération à réaliser avant d'installer l'adaptateur consiste à vérifier que le système est à jour et si ce n'est pas le cas, à le mettre à jour. Pour cela, les deux commandes suivantes permettent de réaliser cette opération :

.. code-block:: bash

  root@beaglebone:~# opkg update
  root@beaglebone:~# opkg upgrade

Ces deux commandes sont à lancer sur le BeagleBone Black depuis un shell connecté avec le compte ``root``. Pour qu'elles réussissent il est également nécessaire que le système puisse télécharger les mises à jour depuis Internet. Il faut donc que le BeagleBone Black soit connecté à Internet, soit via le tethering USB, soit plus simplement en étant connecté via l'interface filaire ethernet.

L'exécution de la commande ``opkg upgrade`` peut être particulièrement longue (2h chez moi), un peu de patience ...

.. code-block:: bash

  ...
  Downloading http://feeds.angstrom-distribution.org/feeds/v2012.12/ipk/eglibc/armv7a-vfp-neon/machine/beaglebone/kernel-firmware-dp83903_3.8.13-r23a.49_beaglebone.ipk.
  Upgrading kernel-module-uio-pruss on root from 3.8.13-r23a.46 to 3.8.13-r23a.49...
  Downloading http://feeds.angstrom-distribution.org/feeds/v2012.12/ipk/eglibc/armv7a-vfp-neon/machine/beaglebone/kernel-module-uio-pruss_3.8.13-r23a.49_beaglebone.ipk.
  Upgrading libproxy on root from 0.4.7-r4.15 to 0.4.7-r4.16...
  Downloading http://feeds.angstrom-distribution.org/feeds/v2012.12/ipk/eglibc/armv7a-vfp-neon/base/libproxy_0.4.7-r4.16_armv7a-vfp-neon.ipk.
  Upgrading libopencv-video2.4 on root from 2.4.2-r3.10 to 2.4.2-r3.11...
  ...

Une fois cette opération terminée, on peut connecter l'adaptateur.

Connexion et installation
-------------------------

Pour connecter un adaptateur Wifi à la carte BeagleBone Black, il est `fortement recommandé <http://www.elinux.org/Beagleboard:BeagleBoneBlack#WIFI_Adapters>`_ d'utiliser une source d'alimentation permettant de fournir au minimum 1A. L'alimentation via le port USB d'un PC en mode "terthered" est donc exclue, le courant fourni étant limité à 500mA. Deux configurations d'alimentation sont donc possibles :

* soit le BeagleBone Black est alimenté par une alimentation 5V externe capable de fournir au minimum 1A;
* ou bien l'adaptateur Wifi est connecté indirectement à la carte via un HUB USB qui fournira l'alimentation à l'adaptateur et donc limitera le courant nécessaire à l'alimentation de la carte.

Une fois l'adaptaeur connecté il suffit de redémarrer le système pour que l'adaptateur soit détecté et le driver chargé (à condition d'avoir choisi un adaptateur supporté par un driver).

.. code-block:: bash

  root@beaglebone:~# shutdown -r now

Au redémarrage, on peut vérifier que le driver a bien été chargé (notez les lignes commençant par ``rtl8192cu``) :

.. code-block:: bash

  root@beaglebone:~# dmesg | grep rtl
  [    9.598467] rtl8192cu 1-1:1.0: usb_probe_interface
  [    9.598495] rtl8192cu 1-1:1.0: usb_probe_interface - got id
  [    9.599763] rtl8192cu: Chip version 0x10
  [   10.601815] rtl8192cu: MAC address: 9c:d6:43:00:b2:a8
  [   10.601845] rtl8192cu: Board Type 0
  [   10.602299] rtlwifi: rx_max_size 15360, rx_urb_num 8, in_ep 1
  [   10.602516] rtl8192cu: Loading firmware rtlwifi/rtl8192cufw.bin
  [   10.602981] usbcore: registered new interface driver rtl8192cu
  [   10.783385] ieee80211 phy0: Selected rate control algorithm 'rtl_rc'
  [   10.784999] rtlwifi: wireless switch is on
  [   10.806975] rtl8192cu: MAC auto ON okay!
  [   10.928611] rtl8192cu: Tx queue select: 0x05

On peut également vérifier la liste des drivers chargés et leurs dépendances avec la commande ``lsmod``:

.. code-block:: bash

  root@beaglebone:~# lsmod
    Module                  Size  Used by
    fuse                   51875  3
    arc4                    1644  2
    rtl8192cu              73616  0
    rtlwifi                63810  1 rtl8192cu
    rtl8192c_common        51159  1 rtl8192cu
    mac80211              270414  3 rtlwifi,rtl8192c_common,rtl8192cu
    cfg80211              166418  2 mac80211,rtlwifi
    g_multi                55905  2
    libcomposite           15228  1 g_multi
    ip_tables               8294  0
    x_tables               15072  1 ip_tables
    rfcomm                 25106  0
    mtnet7601Usta          25701  0
    mt7601Usta            753921  1 mtnet7601Usta
    mtutil7601Usta         65890  2 mt7601Usta,mtnet7601Usta
    ircomm_tty             14503  0
    ircomm                  8846  1 ircomm_tty
    irda                   89974  2 ircomm_tty,ircomm
    ipv6                  229989  12
    hidp                   10112  0
    bluetooth             146100  4 hidp,rfcomm
    rfkill                 16510  5 cfg80211,bluetooth
    autofs4                17432  2

Avec ceux commandes on constate bien que le driver ``rtl8192cu``, utilisé par l'adaptateur DWA-121, est chargé et qu'il est bien utilisé par les services réseaux. Enfin, on peut vérifier que l'interface réseau ``wlan0`` est bien active, mais non configurée :

.. code-block:: bash

  root@beaglebone:~# ifconfig wlan0
    wlan0     Link encap:Ethernet  HWaddr 9C:D6:43:00:B2:A8
            UP BROADCAST MULTICAST  MTU:1500  Metric:1
            RX packets:0 errors:0 dropped:0 overruns:0 frame:0
            TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
            collisions:0 txqueuelen:1000
            RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)


Configuration de la connexion Wifi
----------------------------------

La configuration de la connexion à un réseau Wifi varie d'une distribution à l'autre. Les BeagleBone Black étant actuellement livrés avec la distribution Angstrom Linux, c'est cette configuration que j'aborderai.

La distribution Angstrom utilise le gestionnaire de configuration `connman <https://connman.net/>`_. Ce outil s'utilise normalement au travers d'une interface graphique, mais il est tout à fait possible de le configurer en ligne de commande gràce à un ensemble de scripts disponibles dans le répertoire ``/usr/lib/connman/test/``. Par exemple, la commande suivante permet de lister les services réseaux détectés et notamment la liste des points d'accès Wifi détectés :

.. code-block:: bash

  root@beaglebone:/var/lib/connman# /usr/lib/connman/test/test-connman services
     freebox_XXXXXX             { wifi_9cd64300b2a8_66726565626f785f5142424e5558_managed_psk }
     FreeWifi_secure            { wifi_9cd64300b2a8_46726565576966695f736563757265_managed_ieee8021x }
     FreeWifi                   { wifi_9cd64300b2a8_4672656557696669_managed_none }

Pour créer une connexion sur un de ces points d'accès il faut ensuite créer un fichier de configuration (par exemple ``wifi.cfg``) dans le répertoire ``/var/lib/connman`` contenant les informations suivantes :

.. code-block:: ini

  [service_wifi]
  Type=wifi
  Name=freebox_XXXXXX
  Security=wpa
  Passphrase=***
  AutoConnect=true
  Favorite=true

Il n'y a plus qu'à redémarrer le système et vérifier que l'interface est dorénavant connectée au réseau wifi et bien configurée :

.. code-block:: bash

  wlan0     Link encap:Ethernet  HWaddr 9C:D6:43:00:B2:A8
            inet addr:192.168.1.20  Bcast:192.168.1.255  Mask:255.255.255.0
            inet6 addr: fe80::9ed6:43ff:fe00:b2a8/64 Scope:Link
            UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
            RX packets:128 errors:0 dropped:0 overruns:0 frame:0
            TX packets:41 errors:0 dropped:0 overruns:0 carrier:0
            collisions:0 txqueuelen:1000
            RX bytes:13051 (12.7 KiB)  TX bytes:9477 (9.2 KiB)

Dernier conseil
---------------

Pour réaliser cette configuration je vous conseille de ne pas vous connecter au BeagleBone Black par le cable ethernet filaire mais d'utiliser le mode tethering via USB.

En effet, dans ce cas il y a de fortes chances (selon votre configuration réseau) que l'adaptateur Wifi se trouve connecté au même réseau IP que la connexion Ethernet. Dans cette configuration connman désactivera systématiquement l'une des deux interfaces et vous risquez de chercher longtemps pourquoi la connexion Wifi ne s'établie pas alors que tout vos paramètres sont corrects.
