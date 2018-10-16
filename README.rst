nested_lookup
#############

.. image:: https://img.shields.io/badge/pypi-0.1.7-green.svg
  :target: https://pypi.python.org/pypi/nested-lookup

A small Python library which enables:

#. key lookups on deeply nested documents.
#. fetching all keys from a nested dictionary.
#. get the number of occurrences of a key/value from a nested dictionary

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

 >>> from nested_lookup import get_occurrence_of_key, get_occurrence_of_value

 >>> get_occurrence_of_key(document, key='taco')
 2

 >>> get_occurrence_of_value(document, value='42')
 1

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

To get a list of every nested key in a document, run this:

.. code-block:: python

  from nested_lookup import get_all_keys

  keys = get_all_keys(my_document)

  print(keys)

.. code-block:: python
  
  ['name', 'email_address', 'other', 'secondary_email', 'EMAIL_RECOVERY', 'email_address']

To get the number of occurrence of the given key/value

.. code-block:: python

  from nested_lookup import get_occurrence_of_key, get_occurrence_of_value

  no_of_key_occurrence = get_occurrence_of_key(my_document, key='email_address')

  print(no_of_key_occurrence)  # result => 2

  no_of_value_occurrence = get_occurrence_of_value(my_document, value='test2@example.com')

  print(no_of_value_occurrence)  # result => 1

Next, we could act `wild` and find all the email addresses like this:

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


misc
========

:license:
  * Public Domain

:authors:
  * Russell Ballestrini
  * Douglas Miranda
  * Ramesh RV

:web:
  * http://russell.ballestrini.net
  * http://douglasmiranda.com
  * https://gist.github.com/douglasmiranda/5127251
