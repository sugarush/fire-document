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

    def test_fromkeys(self):
        doc = Document.fromkeys(['test', 'ing'], 'value')
        self.assertDictEqual(doc, {'test': 'value', 'ing': 'value'})
        self.assertTrue(isinstance(doc, Document))

    def test_get(self):
        value = self.doc.get('alpha')
        self.assertEqual(value, self.test_data['alpha'])
        value = self.doc.get('nonexistent', 'test')
        self.assertEqual(value, 'test')
        value = self.doc.get('nonexistent')
        self.assertIsNone(value)

    def test_items(self):
        items = self.doc.items()
        self.assertEqual(items, [
            ('alpha', 'a'),
            ('beta', 'b'),
            ('gamma', 'g'),
            ('delta', {'epsilon': 'e', 'zeta': 'z'})
        ])

    def test_values(self):
        values = self.doc.values()
        self.assertEqual(values, [
            'a',
            'b',
            'g',
            {'epsilon': 'e', 'zeta': 'z'}
        ])

    def test_iteritems(self):
        iteritems = self.doc.iteritems()
        self.assertTrue(isgenerator(iteritems))

    def test_itervalues(self):
        itervalues = self.doc.itervalues()
        self.assertTrue(isgenerator(itervalues))

    def test_pop(self):
        value = self.doc.pop('alpha')
        self.assertEqual(value, self.test_data['alpha'])
        value = self.doc.pop('nonexistent', 'test')
        self.assertEqual(value, 'test')
        value = self.doc.pop('nonexistent')
        self.assertIsNone(value)

    def test_popitem(self):
        k, v = self.doc.popitem()
        self.assertIsNotNone(k)
        self.assertIsNotNone(v)

    @skip('not tested')
    def test_viewitems(self):
        pass

    @skip('not tested')
    def test_viewvalues(self):
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

    @skip('not tested')
    def test_getslice(self):
        pass

    def test_iter(self):
        gen = iter(self.docs)
        self.assertTrue(isgenerator(gen))
        self.assertTrue(isinstance(next(gen), Document))

    #@skip('not tested')
    def test_pop(self):
        value = self.docs.pop()
        self.assertEqual(value, self.test_data[len(self.test_data) - 1])
        value = self.docs.pop(0)
        self.assertEqual(value, self.test_data[0])
        self.docs.pop()
        with self.assertRaises(IndexError):
            self.docs.pop()
