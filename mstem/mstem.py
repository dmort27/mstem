"""Stems tokens until they are in the lexicon or the rules are exhausted."""

import csv
import os.path
import re
from collections import deque

import pkg_resources


class MalformedRuleError(Exception):
    """Exception raised when rules are ill-formed."""

    pass


class Stemmer:
    """Stems words that are not in lexicon.

    Args:
        rule_fn (str): Either the name of a rule set or the path to a rule set
            file.
        lex_fn (list): A list of paths to lexicon files. These files should be
            tab-delimited and contain forms in the language in question in they
            first column.
    """

    def __init__(self, rule_fn, lex_fns=[], delimiter='\t'):
        """Initialize lexicon and rules."""
        self.lexicon = self._read_lex(lex_fns, delimiter)
        self.rules = self._read_rules(rule_fn)
        self.class_re = re.compile(r'\{\{[A-Z]+\}\}')

    def _read_lex(self, lex_fns, delimiter):
        lexicon = set()
        for fn in lex_fns:
            with open(fn, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    records = line.split(delimiter)
                    lexicon.add(records[0])
        return lexicon

    def _read_rules(self, rule_fn):
        # Compute the path of the rules file if it is in the package.
        rel_path = os.path.join('rules', rule_fn + '.tsv')
        abs_path = pkg_resources.resource_filename(__name__, rel_path)
        # Try to use the filename rule_fn as a path outside the package first.
        if os.path.exists(rule_fn):
            fn = rule_fn
        # If this fails, try to find a relevant file within the package.
        elif os.path.exists(abs_path):
            fn = abs_path
        # If neither of these works, raise an exception.
        else:
            raise FileNotFoundError('No such file: {}'.format(abs_path))
        rules = []
        with open(fn, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader)
            for (a, b, gloss) in reader:
                if a[0] == '^':
                    pos = 'prefix'
                elif a[-1] == '$':
                    pos = 'suffix'
                else:
                    raise MalformedRuleError('No edge specified in {}'
                                             .format(a))
                a_re = re.compile(a)
                rules.append((pos, a_re, b, gloss))
        return rules

    def stem(self, token):
        """Stem a token until it is in the lexicon or no rules are left.

        Args:
            token (str): A word to be stemmed.

        Returns:
            str: ``token`` to which stemming rules have been applied.
        """
        for (_, a_re, b, __) in self.rules:
            if token in self.lexicon:
                break
            token = a_re.sub(b, token)
        return token

    def _add_morpheme(gloss, morphemes, pos, m, gl):
        return morphemes

    def _parse(self, token, gloss=False):
        prefixes, suffixes = deque(), deque()
        for pos, a_re, b, gl in self.rules:
            if token in self.lexicon:
                break
            if a_re.search(token):
                m = a_re.search(token).group(0)
                if not self.class_re.match(m):
                    affix = gl if gloss else m
                    if pos == 'suffix':
                        suffixes.appendleft(affix)
                    else:
                        prefixes.append(affix)
                token = a_re.sub(b, token, 1)
        return (prefixes, token, suffixes)

    def parse(self, token, gloss=False):
        """Parse a token into a list of stem and suffixes.

        Args:
            token (str): A word to be parsed.
            gloss (bool): if True, list glosses instead of suffixes.

        Returns:
            list: stem followed by suffixes or glosses, as defined by the
            rules in the rule set.
        """
        prefixes, token, suffixes = self._parse(token, gloss)
        morphemes = deque()
        morphemes.extend(prefixes)
        morphemes.append(token)
        morphemes.extend(suffixes)
        return list(morphemes)

    def segment(self, token):
        """Parse a token into stem and suffix group.

        This method takes a token as input and returns a tuple consisting of
        a stem and suffix group (a string consisting of suffixes with no
        delimiter).

        Args:
            token (str): A word to be segmented.

        Returns:
            tuple: prefix group, root, and suffix group.
        """
        prefixes, stem, suffixes = self._parse(token)
        return (''.join(prefixes), stem, ''.join(suffixes))

    def gloss(self, token):
        """Parse a token into a stem and a sequence of glosses.

        Args:
            token (str): A word to be glossed.

        Returns:
            list: stem followed by glosses for each suffix.

        """
        return self.parse(token, gloss=True)
