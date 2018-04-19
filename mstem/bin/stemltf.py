#!/usr/bin/env python3

import argparse
import glob
import os.path

import lxml.etree as ET

import mstem


def main(dir_in, dir_out, rules, lexicons):
    """Run stemmer on every token in every LTF file."""
    stemmer = mstem.Stemmer(rules, lexicons)
    for fnin in glob.glob(os.path.join(dir_in, '*.ltf.xml')):
        fnout = os.path.join(dir_out, os.path.split(fnin)[1])
        tree = ET.parse(fnin)
        root = tree.getroot()
        for token in root.xpath('//TOKEN'):
            token.text = stemmer.stem(token.text)
        with open(fnout, 'w', encoding='utf-8') as fout:
            xml = ET.tostring(tree, pretty_print=True, encoding='unicode')
            fout.write(xml)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Stem tokens in LTFs')
    parser.add_argument('input_dir',
                        help='directory where input files are located')
    parser.add_argument('output_dir',
                        help='directory for output files')
    parser.add_argument('-r', '--rules', default='ben-Beng',
                        help='rules file')
    parser.add_argument('-l', '--lexicon', nargs='+', default=[],
                        help='lexicon files')
    args = parser.parse_args()
    main(args.input_dir, args.output_dir, args.rules, args.lexicon)
