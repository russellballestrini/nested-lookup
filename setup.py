# installation: pip install nested-lookup

from setuptools import setup

from pip.req import parse_requirements

# get list of requirement strings from requirements.txt
install_requirements =  parse_requirements('requirements.txt', session='None')
requires = map(lambda ir : str(ir.req), install_requirements)

setup( 
    name = 'nested-lookup',
    version = '0.0.3',
    description = 'lookup a key in a deeply nested document of dicts and lists',
    keywords = 'nested document dictionary dict list lookup schema json xml yaml',
    long_description = open('README.rst').read(),

    author = 'Russell Ballestrini',
    author_email = 'russell@ballestrini.net',
    url = 'https://github.com/russellballestrini/nested-lookup',

    platforms = ['All'],
    license = 'Public Domain',

    py_modules = ['nested_lookup'],
    include_package_data = True,
    install_requires = requires,
)

# setup keyword args: http://peak.telecommunity.com/DevCenter/setuptools

# built and uploaded to pypi with this:
# python setup.py sdist bdist_egg register upload
