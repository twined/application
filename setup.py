# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='application',
    version='0.1.0',
    author=u'Twined',
    author_email='www.twined.net',
    packages=find_packages(),
    include_package_data=True,
    url='http://github.com/twined/application',
    license='Do what thou wilt.',
    description='Main admin interface and app inheritance for Twined apps',
    long_description=open('README.md').read(),
    zip_safe=False,
)
