nested_lookup
#############

A small library for python which enables key lookups on deeply nested documents.

Documents may be built out of dictionaries (dicts) and/or lists.

.. contents::



quick start
===========

install
-------

install from pypi using pip::

 pip install nested-lookup

or easy_install::

 easy_install nested-lookup

or install from source using::

 git clone https://github.com/russellballestrini/nested-lookup.git
 cd nested-lookup
 pip install .

tutorial
--------

.. code-block:: python

 >>> from nested_lookup import nested_lookup
 >>> document = [ { 'nachos' : 15 } , { 'salsa' : [ { 'taco': 42 }, { 'burrito' : { 'taco' : 69 } } ] } ]
 >>> print(nested_lookup('taco', document))
 [42, 69]

misc
----

:author: Russell Ballestrini

:web: http://russell.ballestrini.net

:license: Public Domain
