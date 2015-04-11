#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='periscope-firehose',
    version='0.0.1',
    description='Listener for new public Periscope streams',
    long_description=open('README.md').read(),
    author='Anastasis Germanidis',
    author_email='agermanidis@gmail.com',
    packages=['periscope_firehose'],
    install_requires=[
        'requests>=2.4.3',
        'simplejson>=3.6.5',
        'beautifulsoup4>=4.3.2'
    ],
    license=open('LICENSE').read()
)
