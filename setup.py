#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys
from setuptools import setup, find_packages
import django_cloudinary

version = django_cloudinary.get_version()

if sys.argv[-1] == 'publish':
    os.system('python setup.py bdist_wheel upload -r natgeo')
    print("You probably want to also tag the version now:")
    print("  python setup.py tag")
    sys.exit()
elif sys.argv[-1] == 'tag':
    cmd = "git tag -a %s -m 'version %s';git push --tags" % (version, version)
    os.system(cmd)
    sys.exit()


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    """Return the README file contents. Supports text, markdown, and rst"""
    for name in ('README', 'README.md', 'README.rst'):
        if os.path.exists(name):
            return read_file(name)
    return ''

# Use the docstring of the __init__ file to be the description
DESC = " ".join(django_cloudinary.__doc__.splitlines()).strip()

setup(
    name="django-cloudinary",
    version=version.replace(' ', '-'),
    url='https://github.com/natgeosociety/django-cloudinary',
    author='Dan Frakes',
    author_email='dfrakes_c@ngs.org',
    description=DESC,
    long_description=get_readme(),
    packages=find_packages(exclude=['example*', ]),
    include_package_data=True,
    install_requires=read_file('requirements.txt'),
    classifiers=[
        'Framework :: Django',
    ],
)
