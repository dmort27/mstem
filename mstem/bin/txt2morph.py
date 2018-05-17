#!/usr/bin/env python3
from __future__ import print_function

import sys
import mstem
import epitran


def main(fnin):
    epi = epitran.Epitran('hin-Deva')
    st = mstem.Stemmer('hin-IPA', ['../lexicons/hin.tsv'])
    with open(fnin, encoding='utf-8') as fin:
        for line in fin:
            for token in line.split(' '):
                ipa = epi.transliterate(token)
                parse = st.gloss(ipa)
                lemma = parse[0]
                morph = '+'.join(parse[1:])
                print('w:{}~l:{}~m:{}~ipa:{}'.format(token, lemma, morph, ipa))
            print()


if __name__ == '__main__':
    main(sys.argv[1])
