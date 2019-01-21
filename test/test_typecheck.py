from unittest import TestCase

from sugar_document import typecheck, Document, Documents


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
