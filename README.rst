nested_lookup
#############

.. image:: https://img.shields.io/badge/pypi-0.3.0-green.svg
  :target: https://pypi.python.org/pypi/nested-lookup

Python library which enables:

#. (nested_lookup) key lookups on deeply nested documents.
#. (get_all_keys) fetching all keys from a nested dictionary.
#. (get_occurrence_of_key/get_occurrence_of_value) get the number of occurrences of a key/value from a nested dictionary
#. (nested_get) Get a value in a nested document using its key
#. (nested_update) Update a value in a nested document using its key
#. (nested_delete) Delete a key->value pair in nested document using its key

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

 >>> from nested_lookup import nested_get, nested_update, nested_delete

 >>> nested_get(document, 'taco')
 42

 >>> nested_update(document, key='burrito', value='Test')
 [{'taco': 42}, {'salsa': [{'burrito': 'Test'}]}]

 >>> nested_delete(document, 'taco')
 [{}, {'salsa': [{'burrito': {}}]}]


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


To Get / Delete / Update a key->value pair in nested document

.. code-block:: python

  from nested_lookup import nested_get, nested_update, nested_delete

  sec_email = nested_get(my_document, 'secondary_email')

  print(sec_email)  # result => test2@example.com

  nested_delete(my_document, 'EMAIL_RECOVERY')

  print(my_document)  # result => {'other': {'secondary_email': 'test2@example.com', 'email_address': 'test4@example.com'}, 'email_address': 'test1@example.com', 'name': 'Russell Ballestrini'}

  nested_update(my_document, key='other', value='Test')

  print(my_document)  # result => {'other': 'Test', 'email_address': 'test1@example.com', 'name': 'Russell Ballestrini'}


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
