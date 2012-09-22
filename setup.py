#!/usr/bin/env python

import os
import setuptools  # for zip_safe and install_requires
from distutils.core import setup


with open('README.rst') as readme:
    long_description = readme.read()


with open('requirements.txt') as reqs:
    install_requires = [
        line for line in reqs.read().split('\n') if (line and not
                                                     line.startswith('--'))
    ]


setup(
    name='gorun',
    version='1.6',
    description='Wrapper on pyinotify for running commands (often tests)',
    long_description=long_description,
    author='Peter Bengtsson',
    author_email='peter@fry-it.com',
    url='http://github.com/peterbe/python-gorun',
    license='BSD',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Build Tools',
    ],
    scripts=['gorun.py'],
    zip_safe=False,
    install_requires=install_requires,
)
