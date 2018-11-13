from six import iteritems
from nested_lookup import _nested_lookup


def nested_get(document, key):
    """
    Method to get the value from a deeply nested document
    Args:
        document: Might be List of Dicts (or) Dict of Lists (or)
         Dict of List of Dicts etc...
        key: Key to look inside the document
    Return:
        Value if found else NULL
    """

    result = list(_nested_lookup(key=key, document=document))
    if result[0]:
        return result[0]
    else:
        return None


def nested_delete(document, key):
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
            nested_delete(document=list_items, key=key)
    elif isinstance(document, dict):
        if document.get(key):
            del document[key]
        for dict_key, dict_value in iteritems(document):
            nested_delete(document=dict_value, key=key)
    return document


def nested_update(document, key, value):
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
            nested_update(document=list_items, key=key, value=value)
    elif isinstance(document, dict):
        if document.get(key):
            document[key] = value
        for dict_key, dict_value in iteritems(document):
            nested_update(document=dict_value, key=key, value=value)
    return document
