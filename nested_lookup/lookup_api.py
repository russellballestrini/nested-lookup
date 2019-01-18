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
    if not in_place:
        document = copy.deepcopy(document)
    return _nested_update(document=document, key=key, value=value)


def _nested_update(document, key, value):
    """
    Method to update a key->value pair in a nested document
    Args:
        document: Might be List of Dicts (or) Dict of Lists (or)
         Dict of List of Dicts etc...
        key: Key to update the value
    Return:
        Returns a document that has updated key, value pair.
    """
    if isinstance(document, list):
        for list_items in document:
            _nested_update(document=list_items, key=key, value=value)
    elif isinstance(document, dict):
        if document.get(key):
            document[key] = value
        for dict_key, dict_value in iteritems(document):
            _nested_update(document=dict_value, key=key, value=value)
    return document
