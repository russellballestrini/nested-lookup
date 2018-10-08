# installation: pip install nested-lookup

from setuptools import (
  setup,
  find_packages,
)

# get list of requirement strings from requirements.txt
remove_whitespace = lambda x : ''.join(x.split())
sanitize = lambda x : not x.startswith('#') and x != ''
with open('requirements.txt', 'r') as f:
    requires = filter(sanitize, map(remove_whitespace, f.readlines() ))

setup( 
    name = 'nested-lookup',
    version = '0.1.7',
    description = 'lookup a key in a deeply nested document of dicts and lists',
    keywords = 'nested document dictionary dict list lookup schema json xml yaml',
    long_description = open('README.rst').read(),

    author = 'Russell Ballestrini',
    author_email = 'russell@ballestrini.net',
    url = 'https://github.com/russellballestrini/nested-lookup',

    platforms = ['All'],
    license = 'Public Domain',

    packages = find_packages(),
    include_package_data = True,

    install_requires = requires,

    classifiers = [
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

# setup keyword args: http://peak.telecommunity.com/DevCenter/setuptools

# built and uploaded to pypi with this:
# python setup.py sdist bdist_egg register upload
