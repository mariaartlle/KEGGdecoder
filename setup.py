#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='KEGGdecoder',
    version='1.3-modified',
    description='',
    packages=find_packages(),
    # packages=['os', 'matplotlib', 'argparse', 'pandas', 'scipy'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
)
