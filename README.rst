nested_lookup
#############

.. image:: https://img.shields.io/badge/pypi-0.1.1-green.svg
  :target: https://pypi.python.org/pypi/nested-lookup
  
.. image:: https://img.shields.io/badge/coverage-100%-green.svg
  :target: https://github.com/russellballestrini/nested-lookup/blob/master/test_nested_loopkup.py

A small Python library which enables key lookups on deeply nested documents.

Documents may be built out of dictionaries (dicts) and/or lists.

Make working with JSON, YAML, and XML document responses fun again!

.. contents::


install
========

install from pypi using pip::

 pip install nested-lookup

or easy_install::

 easy_install nested-lookup

or install from source using::

 git clone https://github.com/russellballestrini/nested-lookup.git
 cd nested-lookup
 pip install .

tutorial
========

.. code-block:: python

 >>> from nested_lookup import nested_lookup

 >>> document = [ { 'taco' : 42 } , { 'salsa' : [ { 'burrito' : { 'taco' : 69 } } ] } ]

 >>> print(nested_lookup('taco', document))
 [42, 69]

misc
========

:license: 
  * Public Domain

:authors: 
  * Russell Ballestrini
  * Douglas Miranda

:web: 
  * http://russell.ballestrini.net
  * http://douglasmiranda.com
  * https://gist.github.com/douglasmiranda/5127251

