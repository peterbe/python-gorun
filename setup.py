#!/usr/bin/env python

import os
from distutils.core import setup

setup(name = 'python-gorun',
        version = '0.2',
        description = 'Wrapper on pyinotify for running commands (often tests)',
        long_description = file(
            os.path.join(os.path.dirname(__file__), 'README.md')
        ).read(),
        author='Peter Bengtsson',
        author_email='peter@fry-it.com',
        url = 'http://github.com/peterbe/python-gorun',
        classifiers = [
             'Programming Language :: Python :: 2',
             'Intended Audience :: Developers',
             'Operating System :: POSIX :: Linux',
             'Topic :: Software Development :: Testing'
             'Topic :: Software Development :: Build Tools'
       ],
       scripts = ['gorun.py']
)
