Integrating Yuml in Sphinx documentation
########################################

:date: 2013-08-25 22:22
:tags: general
:author: Nico
:summary: This blog entry is about an sphinx extension I wrote to embed Yuml UML diagrams in Sphinx documentation.

Yuml_ is an online tool for generating UML diagrams. It uses a simple API and a descriptive language to generate PNG, JPG, SWF of PDF for class, activity or use case diagrams. See their `samples pages <http://yuml.me/diagram/scruffy/class/samples>`_ for a overviex of Yuml_features.

As I've just been starting to write `specifications for BrewBox <http://brewbox-doc.readthedocs.org/en/latest/>`_ I was looking for an UML diagraming tool. Among the alternatives, Yuml came up because of its simplicity. For example, here is a simple example from BrewBox specifications :

  [Brewery]<>-*>[Equipment]
  [Equipment]-*>[Sensor]
  [Sensor]-1>[SamplingConfiguration]
  [Sensor]-1>[ConversionConfiguration]

Sending this text to Yuml_ API will return an image containing the following class diagram:

.. image: http://yuml.me/diagram/scruffy;dir:LR;/class/[Brewery]<>-*>[Equipment], [Equipment]-*>[Sensor], [Sensor]-1>[SamplingConfiguration], [Sensor]-1>[ConversionConfiguration].jpg

.. links
.. _Yuml: http://yuml.me/
.. _Sphinx: http://sphinx-doc.org/