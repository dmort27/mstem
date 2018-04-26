from unittest import TestCase

import mstem


class TestTagalog(TestCase):
    def setUp(self):
        self.stemmer = mstem.Stemmer('tgl-Latn')

    def test_infix_um(self):
        self.assertEqual(self.stemmer.stem('sumulat'), 'sulat')

    def test_infix_in(self):
        self.assertEqual(self.stemmer.stem('tinapos'), 'tapos')
