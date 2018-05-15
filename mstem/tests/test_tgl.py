from unittest import TestCase

import mstem


class TestTagalog(TestCase):
    def setUp(self):
        self.stemmer = mstem.Stemmer('tgl-Latn')

    def test_infix_um(self):
        self.assertEqual(self.stemmer.stem('sumulat'), 'sulat')

    def test_infix_um_red(self):
        self.assertEqual(self.stemmer.stem('sumusulat'), 'sulat')

    def test_infix_in(self):
        self.assertEqual(self.stemmer.stem('tinapos'), 'tapos')

    def test_prefix_pinaka_ma(self):
        self.assertEqual(self.stemmer.stem('pinakamabundok'), 'bundok')

    def test_parse_prefix_pinaka_ma(self):
        self.assertEqual(self.stemmer.parse('pinakamabundok'),
                         ['pinaka', 'ma', 'bundok'])

    def test_segment_prefix_pinka_ma(self):
        self.assertEqual(self.stemmer.segment('pinakamabundok'),
                         ('pinakama', 'bundok', ''))

    def test_pinupuntahan(self):
        self.assertEqual(self.stemmer.stem('pinupuntahan'), 'punta')

    def test_makagagawa(self):
        self.assertEqual(self.stemmer.stem('makagagawa'), 'gawa')

    def test_parse_sumusulat(self):
        self.assertEqual(self.stemmer.parse('sumusulat'),
                         ['um', 'su', 'sulat'])

    def test_parse_pinupuntahan(self):
        self.assertEqual(self.stemmer.parse('pinupuntahan'),
                         ['in', 'pu', 'punta', 'an'])

    def test_parse_inilalagay(self):
        self.assertEqual(self.stemmer.parse('inilalagay'),
                         ['in', 'i', 'la', 'lagay'])
