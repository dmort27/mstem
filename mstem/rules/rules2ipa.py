#!/usr/bin/env python3

import epitran
import sys


def main(mode, fn):
    epi = epitran.Epitran(mode)
    with open(fn, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            a, b, gloss = line.split('\t')
            ipa = epi.transliterate(a)
            print('\t'.join([ipa, a, b, gloss]))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
