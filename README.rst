nested_lookup
#############

.. image:: https://img.shields.io/badge/pypi-0.2.23-green.svg
  :target: https://pypi.python.org/pypi/nested-lookup
.. image:: https://travis-ci.org/rameshrvr/nested-lookup.svg?branch=master
  :target: https://travis-ci.org/rameshrvr/nested-lookup

Make working with JSON, YAML, and XML document responses fun again!

The `nested_lookup` package provides many Python functions for working with deeply nested documents.
A document in this case is a a mixture of Python dictionary and list objects typically derived from YAML or JSON.

*nested_lookup:*
  Perform a key lookup on a deeply nested document.
  Returns a ``list`` of matching values.

*nested_update:*
  Given a document, find all occurences of the given key and update the value.
  By default, returns a copy of the document.
  To mutate the original specify the ``in_place=True`` argument.

*nested_delete:*
  Given a document, find all occurrences of the given key and delete it.
  By default, returns a copy of the document.
  To mutate the original specify the ``in_place=True`` argument.
  
*nested_alter:*
  Given a document, find all occurrences of the given key and alter it with a callback function.
  By default, returns a copy of the document.
  To mutate the original specify the ``in_place=True`` argument.

*get_all_keys:*
  Fetch all keys from a deeply nested dictionary.
  Returns a ``list`` of keys.

*get_occurrence_of_key/get_occurrence_of_value:*
  Returns the number of occurrences of a key/value from a nested dictionary.

For examples on how to invoke these functions, please check out the tutorial sections.


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

This tutorial uses the Python Interactive shell, please follow along : )

Before we start, let's define an example document to work on.

.. code-block:: python

 >>> document = [ { 'taco' : 42 } , { 'salsa' : [ { 'burrito' : { 'taco' : 69 } } ] } ]


First, we lookup a key from all layers of a document using ``nested_lookup``:

.. code-block:: python

 >>> from nested_lookup import nested_lookup
 >>> print(nested_lookup('taco', document))
 [42, 69]
 
As you can see the function returned a list of two integers, these integers are the values from the matched key lookups.

Next, we update a key and value from all layers of a document using ``nested_update``:

.. code-block:: python

 >>> from nested_lookup import nested_update
 >>> nested_update(document, key='burrito', value='test')
 [{'taco': 42}, {'salsa': [{'burrito': 'test'}]}]
 
Here you see that the key ``burrito`` had it's value changed to the string ``'test'``, like we asked.

Finally, we try out a delete operation using ``nested_delete``:

.. code-block:: python

 >>> from nested_lookup import nested_delete
 >>> nested_delete(document, 'taco')
 [{}, {'salsa': [{'burrito': {}}]}]

Perfect, the returned document looks just like we expected!


longer tutorial
======================

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
    "name" : "Rocko Ballestrini",
    "email_address" : "test1@example.com",
    "other" : {
        "secondary_email" : "test2@example.com",
        "EMAIL_RECOVERY" : "test3@example.com",
        "email_address" : "test4@example.com",
     },
 },

Next, we could act ``wild`` and find all the email addresses like this:

.. code-block:: python

 results = nested_lookup(
     key = "mail",
     document = my_document,
     wild = True
 )

 print(results)

.. code-block:: python

 ["test1@example.com", "test4@example.com", "test2@example.com", "test3@example.com"]

Additionally, if you also needed the matched key names, you could do this:

.. code-block:: python

 results = nested_lookup(
     key = "mail",
     document = my_document,
     wild = True,
     with_keys = True,
 )

 print(results)

.. code-block:: python

  {
   "email_address": ["test1@example.com", "test4@example.com"],
   "secondary_email": ["test2@example.com"],
   "EMAIL_RECOVERY": ["test3@example.com"]
  }

We do not mutate input, if we do you found a defect. Please open an issue.

Let's delete and update our deeply nested key / values and see the results:

.. code-block:: python

  from nested_lookup import nested_update, nested_delete

  # result => {'other': {'secondary_email': 'test2@example.com', 'email_address': 'test4@example.com'}, 'email_address': 'test1@example.com', 'name': 'Rocko Ballestrini'}
  result = nested_delete(my_document, 'EMAIL_RECOVERY')
  print(result)

  # result => {'other': 'Test', 'email_address': 'test1@example.com', 'name': 'Rocko Ballestrini'}
  result = nested_update(my_document, key='other', value='Test')
  print(result)


Now let's say we wanted to get a list of every nested key in a document, we could run this:

.. code-block:: python

  from nested_lookup import get_all_keys

  keys = get_all_keys(my_document)
  print(keys)

.. code-block:: python

  ['name', 'email_address', 'other', 'secondary_email', 'EMAIL_RECOVERY', 'email_address']

Also, to get the number of times a key or value occurs in the document, try:

.. code-block:: python

  from nested_lookup import (
      get_occurrence_of_key,
      get_occurrence_of_value,
  )

  # result => 2
  key_occurrence_count = get_occurrence_of_key(my_document, key='email_address')
  print(no_of_key_occurrence)  

  # result => 1
  value_occurrence_count = get_occurrence_of_value(my_document, value='test2@example.com')
  print(no_of_value_occurrence)

To get the number of occurrence and their respective values

.. code-block:: python

  from nested_lookup import get_occurrences_and_values
  
  my_documents = [
        {
            "processor_name": "4",
            "processor_speed": "2.7 GHz",
            "core_details": {
                "total_numberof_cores": "4",
                "l2_cache(per_core)": "256 KB",
            }
        }
    ]

  result = get_occurrences_and_values(my_documents, value='4')

  print(result)
  
  {
	  "4": {
		  "occurrences": 2,
		  "values": [
			  {
				  "processor_name": "4",
				  "processor_speed": "2.7 GHz",
				  "core_details": {
					  "total_numberof_cores": "4",
					  "l2_cache(per_core)": "256 KB"
				  }
			  },
			  {
				  "total_numberof_cores": "4",
				  "l2_cache(per_core)": "256 KB"
			  }
		  ]
	  }
 }





nested_alter tutorial
=====================

*Nested Alter*:
write a callback function which processes a scalar value.
Be aware about the possible types which can be passed to the callback functions.
In this example we can be sure that only int will be passed, in production you should check the type because it could be anything.

Before we start, let's define an example document to work on.

.. code-block:: python

 >>> document = [ { 'taco' : 42 } , { 'salsa' : [ { 'burrito' : { 'taco' : 69 } } ] } ]

.. code-block:: python

 >>> def callback(data):
 >>>     return data + 10 # add 10 to every taco prize

The alter-version only works for scalar input (one dict), if you need to adress a list of dicts, you have to 
manually iterate over those and pass them to nested_update one by one

.. code-block:: python

 >>> out =[]
 >>> for elem in document:
 >>>     altered_document = nested_alter(elem,"taco", callback)
 >>>     out.append(altered_document)

 >>> print(out)
 [ { 'taco' : 52 } , { 'salsa' : [ { 'burrito' : { 'taco' : 79 } } ] } ]

 >>> from nested_lookup import get_all_keys

 >>> get_all_keys(document)
 ['taco', 'salsa', 'burrito', 'taco']

 >>> from nested_lookup import get_occurrence_of_key, get_occurrence_of_value

 >>> get_occurrence_of_key(document, key='taco')
 2

 >>> get_occurrence_of_value(document, value='42')
 1


misc
========

:license:
  * Public Domain

:authors:
  * Russell Ballestrini
  * Douglas Miranda
  * Ramesh RV
  * Salfiii (Florian S.)
  * Matheus Lins

:web:
  * http://russell.ballestrini.net
  * http://douglasmiranda.com (https://gist.github.com/douglasmiranda/5127251)
  * https://github.com/Salfiii
  * https://github.com/matheuslins
