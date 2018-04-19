from setuptools import setup

setup(name='mstem',
      version='0.1',
      description='Basic multilingal stemmer.',
      url='http://github.com/dmort27/mstem',
      download_url='http://github.com/dmort27/mstem/tarball/0.1',
      author='David R. Mortensen',
      author_email='dmortens@cs.cmu.edu',
      license='MIT',
      install_requires=['setuptools',
                        'regex'],
      scripts=['mstem/bin/stemltf.py',
               'mstem/bin/stemconll.py'],
      packages=['mstem'],
      package_dir={'mstem': 'mstem'},
      package_data={'mstem': ['rules/*.tsv']},
      zip_safe=True,
      classifiers=['Operating System :: OS Independent',
                   'Programming Language :: Python :: 3',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Text Processing :: Linguistic']
      )
