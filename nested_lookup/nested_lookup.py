from six import iteritems

from collections import defaultdict


values_list = []


def nested_lookup(key, document, wild=False, with_keys=False):
    """Lookup a key in a nested document, return a list of values"""
    if with_keys:
        d = defaultdict(list)
        for k, v in _nested_lookup(key, document, wild=wild, with_keys=with_keys):
            d[k].append(v)
        return d
    return list(_nested_lookup(key, document, wild=wild, with_keys=with_keys))


def _is_case_insensitive_substring(a, b):
    """return True if `a` is a case insensitive substring of `b`, else False"""
    return str(a).lower() in str(b).lower()


def _nested_lookup(key, document, wild=False, with_keys=False):
    """Lookup a key in a nested document, yield a value"""
    if isinstance(document, list):
        for d in document:
            for result in _nested_lookup(key, d, wild=wild, with_keys=with_keys):
                yield result

    if isinstance(document, dict):
        for k, v in iteritems(document):
            if key == k or (wild and _is_case_insensitive_substring(key, k)):
                if with_keys:
                    yield k, v
                else:
                    yield v
            if isinstance(v, dict):
                for result in _nested_lookup(key, v, wild=wild, with_keys=with_keys):
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
    return _get_occurrence(dictionary=dictionary, item="key", keyword=key)


def get_occurrences_and_values(items, value):
    """
    Method to get occurrence of a value in a nested list of dictionary

    Args:
        items: list of dictionary: Nested dictionary
        value: Value to search for the occurrences

    Return:
        Dict where the key is the value arg and his value is a new
        dict with occurrences and values
    """
    occurrences = {}
    occurrence = 0
    value_list = []

    for item in items:
        occurrence_result, values = _get_occurrence_with_values(dictionary=item, item="value", keyword=value)
        occurrence = occurrence + occurrence_result
        if occurrence_result:
            value_list.extend(values)

    occurrences[value] = {
        'occurrences': occurrence,
        'values': value_list
    }

    return occurrences


def _get_occurrence_with_values(dictionary, item, keyword):
    occurrence = [0]

    result_recursion = _recursion(dictionary, item, keyword, occurrence, True)

    global values_list
    values_list = []

    return occurrence[0], result_recursion


def get_occurrence_of_value(dictionary, value):
    """
    Method to get occurrence of a value in a nested dictionary

    Args:
        dictionary: Nested dictionary
        value: Value to search for the occurrences
    Return:
        Number of occurrence (Integer)
    """
    return _get_occurrence(dictionary=dictionary, item="value", keyword=value)


def _recursion(dictionary, item, keyword, occurrence, with_values=False):

    global values_list

    if item == "key":
        if dictionary.get(keyword) is not None:
            occurrence[0] += 1
    elif keyword in list(dictionary.values()):
        occurrence[0] += list(dictionary.values()).count(keyword)
        if with_values:
            values_list.append(dictionary)
    for key, value in iteritems(dictionary):
        if isinstance(value, dict):
            _recursion(value, item, keyword, occurrence, with_values)
        elif isinstance(value, list):
            for list_items in value:
                if hasattr(list_items, "items"):
                    _recursion(list_items, item, keyword, occurrence, with_values)
                elif list_items == keyword:
                    occurrence[0] += 1 if item == "value" else 0

    if values_list:
        return values_list


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
    _recursion(dictionary, item, keyword, occurrence)

    global values_list
    values_list = []

    return occurrence[0]
