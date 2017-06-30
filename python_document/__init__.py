
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

    def __init__(self, item):
        super(Documents, self).__init__(item)

    def __getitem__(self, index):
        item = super(Documents, self).__getitem__(index)
        return typecheck(item)

    def __iter__(self):
        for item in super(Documents, self).__iter__():
            yield typecheck(item)
