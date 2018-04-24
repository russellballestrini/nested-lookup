from six import iteritems

def nested_lookup(key, document, wild=False, output='dict'):
    """Lookup a key in a nested document, return a list of values"""
    if output == 'dict':
        return dict(_nested_lookup(key, document, wild=wild, output=output))
    elif output == 'list':
        return list(_nested_lookup(key, document, wild=wild, output=output))
    else:
        raise ValueError('Output is of unknown type '+output)

def _nested_lookup(key, document, wild=False, output='dict'):
    """Lookup a key in a nested document, yield a value"""
    if isinstance(document, list):
        for d in document:
            for result in _nested_lookup(key, d, wild=wild):
                yield result

    if isinstance(document, dict):
        for k, v in iteritems(document):
            if key == k or (wild and key.lower() in k.lower()):
                if output == 'dict':
                    yield k, v
                elif output == 'list':
                    yield v
            elif isinstance(v, dict):
                for result in _nested_lookup(key, v, wild=wild, output=output):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in _nested_lookup(key, d, wild=wild, output=output):
                        yield result
