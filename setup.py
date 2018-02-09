#!/usr/bin/env python3
from setuptools import setup
from setuptools import find_packages
pack=find_packages()
setup(name='bioinfoutils',
      version='0.1',
      description='Bioinfoutils',
      long_description = open('README.md').read(),
      url='http://github.com/tobbeost/bioinfoutils',
      author='Tobias Osterlund',
      author_email='tobiaso@chalmers.se',
      packages=pack,
      package_data={'bioinfoutils': ['README.md']
                   },
      include_package_data=True,
      classifiers=['Topic :: Scientific/Engineering :: Bio-Informatics'],
      scripts=['bioinfoutils/readFastaAndCount.py', 
               'bioinfoutils/removeDuplicatedSequences.py'],
      zip_safe=False)