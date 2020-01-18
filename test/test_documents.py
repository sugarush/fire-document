from unittest import TestCase, skip
from inspect import isgenerator

from fire_document import Document, Documents


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
