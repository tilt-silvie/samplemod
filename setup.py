# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='NEED_MODIFY',
    version='0.0.1',
    description='NEED_MODIFY',
    long_description=readme,
    author='Makito Ishikura',
    author_email='tilt.silvie@gmail.com',
    url='NEED_MODIFY',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

