# installation: pip install nested-lookup

from setuptools import setup

setup( 
    name = 'nested-lookup',
    version = '0.0.1',
    description = 'lookup a key in a deeply nested document of dicts and lists',
    keywords = 'nested document dictionary dict list lookup schema json xml',
    long_description = open('README.rst').read(),

    author = 'Russell Ballestrini',
    author_email = 'russell@ballestrini.net',
    url = 'https://github.com/russellballestrini/nested-lookup',

    platforms = ['All'],
    license = 'Public Domain',

    py_modules = ['nested_lookup'],
    include_package_data = True,
)

# setup keyword args: http://peak.telecommunity.com/DevCenter/setuptools

# built and uploaded to pypi with this:
# python setup.py sdist bdist_egg register upload
