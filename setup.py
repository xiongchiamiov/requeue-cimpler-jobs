#!/usr/bin/env python
import os
from distutils.core import setup

from requeue_cimpler_jobs import VERSION

# I really prefer Markdown to reStructuredText.  PyPi does not.  This allows me
# to have things how I'd like, but not throw complaints when people are trying
# to install the package and they don't have pypandoc or the README in the
# right place.
try:
   import pypandoc
   description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   description = ''

setup(
   name = 'requeue-cimpler-jobs',
   version = VERSION,
   author = 'James Pearson',
   author_email = 'pearson@changedmy.name',
   packages = ['requeue_cimpler_jobs'],
   scripts = ['bin/requeue-cimpler-jobs'],
   url = 'https://github.com/xiongchiamiov/requeue-cimpler-jobs',
   license = 'WTFPL',
   description = 'Easily requeue all your cimpler jobs.',
   long_description = description,
   install_requires = [
      'docopt >= 0.6.1',
      'envoy >= 0.0.2',
      'github3.py >= 0.9, < 1.0',
   ],
)

