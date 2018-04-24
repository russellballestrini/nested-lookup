nested_lookup
#############

.. image:: https://img.shields.io/badge/pypi-0.1.3-green.svg
  :target: https://pypi.python.org/pypi/nested-lookup

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


wild
========

We also have a `wild` mode that treats the given `key` as a case insensitive
substring of all the keys in the document and returns any values which match.

For example:

.. code-block:: python

 from nested_lookup import nested_lookup

 my_document = {
    'name' : 'Russell Ballestrini',
    'email_address' : 'test1@example.com',
    'other' : {
        'secondary_email' : 'test2@example.com',
        'EMAIL_RECOVERY' : 'test3@example.com',
     },
 },

 results = nested_lookup(
     key = 'mail',
     document = my_document,
     wild = True
 )

 print(results)
 ['test1@example.com', 'test2@example.com', 'test3@example.com']


output
========

There are two `output` modes:
  - `list`: the function returns a list of values corresponding to the
  matched keys.
  - `dict`: the function returns a `dict` with the matched keys as keys and
  their corresponding values as values.

For example:

.. code-block:: python

 from nested_lookup import nested_lookup

 my_document = {
     'name' : 'Russell Ballestrini',
     'email_address' : 'test1@example.com',
     'other' : {
         'secondary_email' : 'test2@example.com',
         'EMAIL_RECOVERY' : 'test3@example.com',
     },
 },

 results = nested_lookup(
     key = 'mail',
     document = my_document,
     wild = True,
     output = 'dict'
 )

 print(results)
 {'email_address': 'test1@example.com',
 'secondary_email': 'test2@example.com',
 'EMAIL_RECOVERY': 'test3@example.com'}


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
