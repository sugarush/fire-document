from unittest import skip, TestCase
from inspect import isgenerator

from python_document import typecheck, Document, Documents

class TestTypecheck(TestCase):

    test_data = [
        { 'alpha': 'a' },
        { 'beta': 'b' },
        { 'gamma': 'g' },
    ]

    def setUp(self):
        self.docs = typecheck(self.test_data)

    def test_base(self):
        self.assertTrue(isinstance(self.docs[0]['alpha'], str))

    def test_dict(self):
        self.assertTrue(isinstance(self.docs[0], Document))

    def test_list(self):
        self.assertTrue(isinstance(self.docs, Documents))


class TestDocument(TestCase):

    test_data = {
        'alpha': 'a',
        'beta': 'b',
        'gamma': 'g',
        'delta': {
            'epsilon': 'e',
            'zeta': 'z',
        },
    }

    def setUp(self):
        self.doc = Document(self.test_data)

    def test_getattr(self):
        self.assertTrue(isinstance(self.doc['alpha'], str))

    @skip('unnecessary')
    def test_iter(self):
        gen = iter(self.doc)
        self.assertTrue(isgenerator(gen))
        self.assertTrue(isinstance(next(gen), str))
        print next(gen)

    @skip('not tested')
    def test_items(self):
        pass

    @skip('not tested')
    def test_values(self):
        pass

    @skip('not tested')
    def test_iteritems(self):
        pass

    @skip('not tested')
    def test_itervalues(self):
        pass

class TestDocuments(TestCase):

    test_data = [
        { 'alpha': 'a' },
        { 'beta': 'b' },
        { 'gamma': 'g' },
    ]

    def setUp(self):
        self.docs = Documents(self.test_data)

    def test_init(self):
        map(self.assertDictEqual, self.docs, self.test_data)

    def test_getitem(self):
        docs = Documents(self.test_data)
        self.assertDictEqual(docs[0], self.test_data[0])

    def test_iter(self):
        gen = iter(self.docs)
        self.assertTrue(isgenerator(gen))
        self.assertTrue(isinstance(next(gen), Document))
