# README for MStem

MStem is a Python 3 implementation of morphological stemming. It consists of a single class, Stemmer, that is instantiated with a list of lexicon files (tab separated with the language to be stemmed in the first column) and a file containing a list of rules (tab separated and of the form a<tab>b<tab>gloss where a is a regular expression to match, b is a string that should replace it, and gloss is a descriptive gloss for the rule).

Replacements that are enclosed in double curly brackets have a special meaning. These are used to enforce "position class" behavior. For example, case suffixes may be replaced with "{{CASE}}" and, when all case rules have been applied, "{{CASE}}" can then be replace with the empty string. This prevents the stemmer from applying multiple case rules since there can typically only be one case marker.

Note that MStem really only suitable for parsing off inflectional prefixes and suffixes. Support for some infixes can be added, but it is not suitable for templatic morphology or infixes with complex prosodic subcategorization. The whole approach doesn't make sense for derivational morphology.

## Usage

You may instantiate the `Stemmer` class with either a mode (like `ben-Beng` for Bengali in Bengali script) or a path (like `mstem/rules/ben-IPA.tsv`) to specify a rules file.

```
>>> import mstem
>>> stemmer1 = mstem.Stemmer('ben-IPA')
>>> stemmer2 = mstem.Stemmer('mstem/rules/ben-Beng.tsv')
```

A list of lexicon files is optional, but highly recommended (since they will prevent some over-stemming). For reasons of licensing, lexicons cannot usually be distributed with MStem, so they will always be paths to external files:

```
>>> stemmer3 = mstem.Stemmer('ben-IPA', ['mstem/lexicons/ben-IPA_lexicon.tsv'])
>>> stemmer4 = mstem.Stemmer('ben-Beng', ['mstem/lexicons/ben-Beng_lexicon.tsv'])
```

Usage for stemming is as follows:

```
>>> stemmer3.stem('patkʰiʈi')
'patkʰi'
>>> stemmer4.stem('কান্দাহারের')
'কান্দাহারে'
```

If, rather than just a stem, you would like a <stem, suffix_string> tuple, call the `Stemmer.segment` method instead:

```
>>> stemmer3.parse('patkʰiʈi')
('patkʰi', 'ʈi')
```

Finally, if you would like a list consisting of a stem and 0 or more suffixes, you can call the `Stemmer.parse` method:

```
>>> stemmer3.segment('gurujoner')
['guru', 'jon', 'er']
```

## Rule files

Included are two rule files:

* `ben-IPA` for stemming Bengali IPA.
* `ben-Beng` for stemming Bengali orthography (surface form).

## Lexicon files

Lexicon files are tab-delimited files where the first column contains lemmas in the language to be stemmed. No other columns need to be present and all other columns will be ignored. The order of entries in a lexicon file is not significant.

## Utility scripts

### `stemltf.py`

`stemltf.py` is a utility script for stemming tokens in LTF files. It's usage is as follows:

```
$ stemltf.py ltf/ ltf-stemmed/ -r ben-IPA -l lexicon1.tsv lexicon2.tsv
```

Where `ltf/` is the directory containing the LTF files to process and `ltf-stemmed` is the directory to which the stemmed LTFs are to be written. Because there can be any number of lexicons, this argument must come after the positional arguments (directories for input and output files).

### `stemconll.py`

`stemconll.py` is a utility script for stemming tokens in CONLL files. A usage example follows:

```
$ stemconll ben.conll -r ben-Beng -l lexicon1.tsv lexicon2.tsv > ben_stemmed.conll
```

`ben.conll` is the input file. By default, it is assumed that the file is tab-delimited. If it is space delimited, you can specify an additional option `-d ' '`. `ben-Beng` is the ruleset to be applied. The list of lexicons is given with the `-l` or `--lexicon` option. Output is written to STDOUT. In this case, it is redirected to a file, `ben_stemmed.conll`.
