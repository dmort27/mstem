from unittest import TestCase

import mstem


class TestBenIPA(TestCase):
    def setUp(self):
        self.stemmer = mstem.Stemmer('ben-IPA')

    def test_stem_ben_ipa(self):
        self.assertTrue(self.stemmer.stem('gurujoner'), 'guru')

    def test_parse_ben_ipa(self):
        self.assertTrue(self.stemmer.parse('gurujoner'), ['guru', 'jon', 'er'])

    def test_segment_ben_ipa(self):
        self.assertTrue(self.stemmer.segment('gurujoner'),
                        ('', 'guru', 'joner'))

    def test_parse_wp_ben_ipa(self):
        self.assertTrue(self.stemmer.parse_wp('gurujoner'),
                        ('guru', {'CL', 'GEN'}))


class TestBenBeng(TestCase):
    def setUp(self):
        self.stemmer = mstem.Stemmer('ben-Beng')

    def test_stem_ben_beng(self):
        self.assertTrue(self.stemmer.stem('গুরুযোনের'), 'গুরু')

    def test_parse_ben_beng(self):
        self.assertTrue(self.stemmer.parse('গুরুযোনের'), ['গুর', 'যোন', 'ের'])

    def test_segment_ben_beng(self):
        self.assertTrue(self.stemmer.segment('গুরুযোনের'),
                        ('', 'গুর', 'যোনের'))
