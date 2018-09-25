nested_lookup
#############

.. image:: https://img.shields.io/badge/pypi-0.1.5-green.svg
  :target: https://pypi.python.org/pypi/nested-lookup

A small Python library which enables:
1. key lookups on deeply nested documents.
2. fetching all keys from a nested dictionary.

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

quick tutorial
==============

.. code-block:: python

 >>> from nested_lookup import nested_lookup

 >>> document = [ { 'taco' : 42 } , { 'salsa' : [ { 'burrito' : { 'taco' : 69 } } ] } ]

 >>> print(nested_lookup('taco', document))
 [42, 69]

 >>> from nested_lookup import get_all_keys

 >>> get_all_keys(document)
 ['taco', 'salsa', 'burrito', 'taco']

longer tutorial
===============

You may control the function's behavior by passing some optional arguments.

wild (defaults to `False`):
 if `wild` is `True`, treat the given `key` as a case insensitive
 substring when performing lookups.

with_keys (defaults to `False`):
  if `with_keys` is `True`, return a dictionary of all matched keys
  and a list of values.

For example, given the following document:

.. code-block:: python

 from nested_lookup import nested_lookup

 my_document = {
    'name' : 'Russell Ballestrini',
    'email_address' : 'test1@example.com',
    'other' : {
        'secondary_email' : 'test2@example.com',
        'EMAIL_RECOVERY' : 'test3@example.com',
        'email_address' : 'test4@example.com',
     },
 },

We could act `wild` and find all the email addresses like this:

.. code-block:: python

 results = nested_lookup(
     key = 'mail',
     document = my_document,
     wild = True
 )

 print(results)

.. code-block:: python

 ['test1@example.com', 'test4@example.com', 'test2@example.com', 'test3@example.com']

Additionally, if you also needed the matched key names, you could do this:

.. code-block:: python

 results = nested_lookup(
     key = 'mail',
     document = my_document,
     wild = True,
     with_keys = True,
 )

 print(results)

.. code-block:: python

  {
   'email_address': ['test1@example.com', 'test4@example.com'],
   'secondary_email': ['test2@example.com'],
   'EMAIL_RECOVERY': ['test3@example.com']
  }


Tutorial to get all keys from a nested dictionary

.. code-block:: python

  sample_data = {
    "hardware_details": {
        "model_name": "MacBook Pro",
        "processor_details": {
            "processor_name": "Intel Core i7",
            "processor_speed": "2.7 GHz",
            "core_details": {
                "total_numberof_cores": "4",
                "l2_cache(per_core)": "256 KB"
            }
        },
        "total_number_of_cores": "4",
        "memory": "16 GB",
    },
    "os_details": {
        "product_version": "10.13.6",
        "build_version": "17G65"
    },
    "name": "Test",
    "date": "YYYY-MM-DD HH:MM:SS"
  }

  result = get_all_keys(sample_data)

  print(result)

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
