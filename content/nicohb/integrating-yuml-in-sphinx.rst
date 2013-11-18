Integrating Yuml in Sphinx documentation
########################################

:date: 2013-08-25 22:22
:tags: python, BrewBox
:author: Nico
:summary: This blog entry is about an sphinx extension I wrote to embed Yuml UML diagrams in Sphinx documentation.


I've just been starting to write `specifications for BrewBox <http://brewbox-doc.readthedocs.org/en/latest/>`_ and I originally chose OmniGraffle_ for designing UML diagrams. After some days using this software I find it not flexible enough, in particular when schemas get bigger. Therefore I've been looking for an (open source) alternative. After some search and study, Yuml_ came up because of its simplicity. 

Yuml_ is an online tool for generating UML diagrams. It uses a simple API and a descriptive language to generate PNG, JPG, SWF of PDF for class, activity or use case diagrams. Have a look at the `samples pages <http://yuml.me/diagram/scruffy/class/samples>`_ for a overview of Yuml_ features. Here is an example, using BrewBox classes : ::

  [Brewery]<>-*>[Equipment]
  [Equipment]-*>[Sensor]
  [Sensor]-1>[SamplingConfiguration]
  [Sensor]-1>[ConversionConfiguration]

Sending this text to Yuml_ API will return an image containing the following class diagram:

.. image:: /static/images/yuml-class-diagram.png
   :alt: BrewBox sample UML diagram
   :align: center

To integrate such diagrams in specification documents I first wanted to create Yuml_ description for every schema and then generate each image using Yuml online. Of course this is a boring and painful activity, so this was a bad idea. Instead of that I thought it could be very nice to be able to write Yuml_ description directly in `restructured sources files <https://github.com/beerfactory/brewbox-doc>`_ and let Sphinx_ automatically convert these descriptions into images using Yuml_ online service. 

Fortunatelly this is possible through Sphinx_ `extension <http://sphinx-doc.org/extensions.html>`_ mechanism. So I decided to go on and write an extension allowing Yuml diagram embedding in Sphinx_ generated documentation. I didn't start from scratch and I used `Gnuplot <https://bitbucket.org/birkenfeld/sphinx-contrib/src/dc99bd08ef54d09be5be8bf6f7692a7fa310778c/gnuplot/?at=default>`_ extension as a model. The extension I wrote is named ``sphinxcontrib-yuml``. It defines a new ``yuml::`` directive which works like the ``image::`` directive except that the image file is not required and generated automatically during compilation by calling Yuml_ service *on-the-fly*.

More concretelly, using ``sphinxcontrib-yuml`` you can write directives like : ::

  .. yuml:: 
	:style: plain 

	[Customer]->[Billing Address]

to automatically get the following image in your documentation :

.. image:: /static/images/yuml-class-diagram2.png
   :alt: BrewBox sample UML diagram
   :align: center

The ``sphinxcontrib-yuml`` extension sources are published on `Github <https://github.com/njouanin/sphinxcontrib-yuml>`_. Python package is available on `Pypi <https://pypi.python.org/pypi/sphinxcontrib-yuml>`_. Documentation and configuration options are described in the `README <https://github.com/njouanin/sphinxcontrib-yuml/blob/master/README.rst>`_ file.

.. links
.. _Yuml: http://yuml.me/
.. _Sphinx: http://sphinx-doc.org/
.. _OmniGraffle: http://www.omnigroup.com/omnigraffle