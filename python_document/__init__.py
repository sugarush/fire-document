
def typecheck(item):
    if isinstance(item, dict):
        return Document(item)
    elif isinstance(item, list):
        return Documents(item)
    return item


class Document(dict):

    def __getattr__(self, name):
        value = self[name]
        return typecheck(value)

    def items(self):
        pass

    def values(self):
        pass

    def iteritems(self):
        for key, value in super(Document, self).iteritems():
            yield (key, typecheck(value))

    def itervalues(self):
        pass


class Documents(list):

    def __init__(self, iterable):
        super(Documents, self).__init__(iterable)

    def __getitem__(self, index):
        value = super(Documents, self).__getitem__(index)
        return typecheck(value)

    def __iter__(self):
        for value in super(Documents, self).__iter__():
            yield typecheck(value)
