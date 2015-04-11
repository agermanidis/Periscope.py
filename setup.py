#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='periscope-firehose',
    version='0.0.6',
    description='Listener for new public Periscope streams',
    long_description=open('README.md').read(),
    author='Anastasis Germanidis',
    author_email='agermanidis@gmail.com',
    packages=['periscope_firehose'],
    install_requires=[
        'requests>=2.4.3',
        'simplejson>=3.6.5',
        'BeautifulSoup>=3.2.1',
        'tweepy>=3.3.0',
        'boto>=2.38.0'
    ],
    license=open('LICENSE').read()
)
