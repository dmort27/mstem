#!/usr/bin/env python3

from lxml import etree
import epitran
import csv
import sys


def main(mode, fnin, fnout):
    epi = epitran.Epitran(mode)
    tree = etree.parse(fnin)
    root = tree.getroot()
    with open(fnout, 'w', encoding='utf-8') as fout:
        writer = csv.writer(fout, dialect='excel-tab')
        for entry in root.xpath('//ENTRY'):
            lemma = entry.find('LEMMA').text
            gloss = entry.find('GLOSS').text
            writer.writerow([epi.transliterate(lemma), gloss])


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
