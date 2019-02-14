import copy
from six import iteritems


def nested_delete(document, key, in_place=False):
    if not in_place:
        document = copy.deepcopy(document)
    return _nested_delete(document=document, key=key)


def _nested_delete(document, key):
    """
    Method to delete a key->value pair from a nested document
    Args:
        document: Might be List of Dicts (or) Dict of Lists (or)
         Dict of List of Dicts etc...
        key: Key to delete
    Return:
        Returns a document that includes everything but the given key
    """
    if isinstance(document, list):
        for list_items in document:
            _nested_delete(document=list_items, key=key)
    elif isinstance(document, dict):
        if document.get(key):
            del document[key]
        for dict_key, dict_value in iteritems(document):
            _nested_delete(document=dict_value, key=key)
    return document


def nested_update(document, key, value, in_place=False):
    """
    Method to update a key->value pair in a nested document
    Args:
        document: Might be List of Dicts (or) Dict of Lists (or)
        Dict of List of Dicts etc...
        key: Key to update the value
    Return:
        Returns a document that has updated key, value pair.
    """

    # check if a list or scalar value is provided and create a list from the scalar value
    # check the length of the list and provide it to _nested_update
    if type(value) == list:
        val_len = len(value)
    else: 
        value  = [value]
        val_len = len(value)

    if not in_place:
        document = copy.deepcopy(document)
    return _nested_update(document=document, key=key, value=value, val_len = val_len)

def _nested_update(document, key, value, val_len, run = 0):
    """
    Method to update a key->value pair in a nested document
    Args:
        document: Might be List of Dicts (or) Dict of Lists (or)
            Dict of List of Dicts etc...
        key (str): Key to update the value
        value (list): value(s) which should be used for replacement purpouse
        val_len (int): lenght of the value element
        run (int): holds the number of findings for the given key. 
            Every time the key is found, run = run + 1. If the list value[run] exists,
            the corresponding element is used for replacement purpouse.
            Defaults to 0.
    Return:
        Returns a document that has updated key, value pair.
    """
    if isinstance(document, list):
        for list_items in document:
            _nested_update(document=list_items, key=key, value=value, val_len = val_len, run = run)
    elif isinstance(document, dict):
        if document.get(key):
            # check if a value with the coresponding index exists and use it otherwise recycle the intially given value
            val = value[run] if run < val_len  else value[0]
            document[key] = val
            run = run + 1
        for dict_key, dict_value in iteritems(document):
            _nested_update(document=dict_value, key=key, value=value, val_len = val_len, run = run)
    return document
