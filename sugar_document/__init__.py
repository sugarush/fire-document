
def typecheck(item):
    if isinstance(item, dict):
        return Document(item)
    elif isinstance(item, list):
        return Documents(item)
    return item


class Document(dict):

    def __getattribute__(self, key):
        if key in self:
            return typecheck(self[key])
        return super(Document, self).__getattribute__(key)

    def __getitem__(self, key):
        value = super(Document, self).__getitem__(key)
        return typecheck(value)

    @classmethod
    def fromkeys(cls, keys, default=None):
        return super(Document, cls).fromkeys(keys, default)

    def get(self, key, default=None):
        value = super(Document, self).get(key, default)
        return typecheck(value)

    def items(self):
        items = super(Document, self).items()
        return [ ( k, typecheck(v) ) for ( k, v ) in items ]

    def values(self):
        values = super(Document, self).values()
        return [ typecheck(v) for v in values ]

    def iteritems(self):
        for key, value in super(Document, self).iteritems():
            yield (key, typecheck(value))

    def itervalues(self):
        for value in super(Document, self).itervalues():
            yield typecheck(value)

    def pop(self, key, default=None):
        value = super(Document, self).pop(key, default)
        return typecheck(value)

    def popitem(self):
        key, value = super(Document, self).popitem()
        return (key, typecheck(value))

class Documents(list):

    def __init__(self, iterable):
        super(Documents, self).__init__(iterable)

    def __getitem__(self, index):
        value = super(Documents, self).__getitem__(index)
        return typecheck(value)

    def __getslice__(self, i, j):
        return super(Documents, self).__getslice__(i, j)

    def __iter__(self):
        for value in super(Documents, self).__iter__():
            yield typecheck(value)

    def pop(self, index=None):
        if index is None:
            index = len(self) - 1
        if index < 0:
            raise IndexError
        value = super(Documents, self).pop(index)
        return typecheck(value)
