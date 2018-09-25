from six import iteritems

from collections import defaultdict


def nested_lookup(key, document, wild=False, with_keys=False):
    """Lookup a key in a nested document, return a list of values"""
    if with_keys:
        d = defaultdict(list)
        for k, v in _nested_lookup(key, document, wild=wild, with_keys=with_keys):
            d[k].append(v)
        return d
    return list(_nested_lookup(key, document, wild=wild, with_keys=with_keys))


def _nested_lookup(key, document, wild=False, with_keys=False):
    """Lookup a key in a nested document, yield a value"""
    if isinstance(document, list):
        for d in document:
            for result in _nested_lookup(key, d, wild=wild, with_keys=with_keys):
                yield result

    if isinstance(document, dict):
        for k, v in iteritems(document):
            if key == k or (wild and key.lower() in k.lower()):
                if with_keys:
                    yield k, v
                else:
                    yield v
            elif isinstance(v, dict):
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

    def recrusion(dictionary):
        for key, value in iteritems(dictionary):
            if isinstance(value, dict):
                result_list.append(key)
                recrusion(dictionary=value)
            elif isinstance(value, list):
                result_list.append(key)
                for list_items in value:
                    recrusion(dictionary=list_items)
            else:
                result_list.append(key)

    recrusion(dictionary=dictionary)
    return result_list
