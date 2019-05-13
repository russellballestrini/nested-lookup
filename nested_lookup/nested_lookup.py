from six import iteritems

from collections import defaultdict


def nested_lookup(key, document, wild=False, with_keys=False):
    """Lookup a key in a nested document, return a list of values"""
    if with_keys:
        d = defaultdict(list)
        for k, v in _nested_lookup(
            key, document, wild=wild, with_keys=with_keys
        ):
            d[k].append(v)
        return d
    return list(_nested_lookup(key, document, wild=wild, with_keys=with_keys))


def _nested_lookup(key, document, wild=False, with_keys=False):
    """Lookup a key in a nested document, yield a value"""
    if isinstance(document, list):
        for d in document:
            for result in _nested_lookup(
                key, d, wild=wild, with_keys=with_keys
            ):
                yield result

    if isinstance(document, dict):
        for k, v in iteritems(document):
            if key == k or (wild and key.lower() in k.lower()):
                if with_keys:
                    yield k, v
                else:
                    yield v
            if isinstance(v, dict):
                for result in _nested_lookup(
                    key, v, wild=wild, with_keys=with_keys
                ):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in _nested_lookup(
                        key, d, wild=wild, with_keys=with_keys
                    ):
                        yield result


def get_all_keys(dictionary):
    """
        Method to get all keys from a nested dictionary as a List
        Args:
            dictionary: Nested dictionary
        Returns:
            List of keys in the dictionary
    """
    result_list = []

    def recrusion(document):
        if isinstance(document, list):
            for list_items in document:
                recrusion(document=list_items)
        elif isinstance(document, dict):
            for key, value in iteritems(document):
                result_list.append(key)
                recrusion(document=value)
        return

    recrusion(document=dictionary)
    return result_list


def get_occurrence_of_key(dictionary, key):
    """
    Method to get occurrence of a key in a nested dictionary

    Args:
        dictionary: Nested dictionary
        key: Key to search for the occurrences
    Return:
        Number of occurrence (Integer)
    """
    return _get_occurrence(dictionary=dictionary, item='key', keyword=key)


def get_occurrence_of_value(dictionary, value):
    """
    Method to get occurrence of a value in a nested dictionary

    Args:
        dictionary: Nested dictionary
        value: Value to search for the occurrences
    Return:
        Number of occurrence (Integer)
    """
    return _get_occurrence(dictionary=dictionary, item='value', keyword=value)


def _get_occurrence(dictionary, item, keyword):
    """
    Method to get occurrence of a key or value in a nested dictionary

    Args:
        dictionary: Nested dictionary
        item: Mostly (key or value)
        keyword: key word to find occurrence
    Return:
        Number of occurrence of the given keyword in the dict
    """
    occurrence = [0]

    def recrusion(dictionary):
        if item == 'key':
            if dictionary.get(keyword) is not None:
                occurrence[0] += 1
        elif keyword in list(dictionary.values()):
            occurrence[0] += list(dictionary.values()).count(keyword)
        for key, value in iteritems(dictionary):
            if isinstance(value, dict):
                recrusion(dictionary=value)
            elif isinstance(value, list):
                for list_items in value:
                    if hasattr(list_items, 'items'):
                        recrusion(dictionary=list_items)
                    elif list_items == keyword:
                        occurrence[0] += 1 if item == 'value' else 0

    recrusion(dictionary=dictionary)
    return occurrence[0]
