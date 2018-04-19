#!/usr/bin/env python3

import argparse

import mstem


def main(fnin, rules, lexicons, delimiter):
    """Run stemmer on every token in a CONLL file, writing result to STDOUT."""
    stemmer = mstem.Stemmer(rules, lexicons)
    with open(fnin, encoding='utf-8') as fin:
        for line in fin:
            line = line.strip()
            if not line:
                print()
                continue
            fields = line.split(delimiter)
            fields[0] = stemmer.stem(fields[0])
            line = delimiter.join(fields)
            print(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Stem tokens in CONLL file')
    parser.add_argument('input_file',
                        help='Input file (CONLL)')
    parser.add_argument('-r', '--rules', default='ben-Beng',
                        help='rules file')
    parser.add_argument('-l', '--lexicon', nargs='+', default=[],
                        help='lexicon files')
    parser.add_argument('-d', '--delimiter', default='\t',
                        help='Delimiter (defaults to tab)')
    args = parser.parse_args()
    main(args.input_file, args.rules, args.lexicon, args.delimiter)
