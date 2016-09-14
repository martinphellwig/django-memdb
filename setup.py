"""
PyPi Setup file.
"""
# pylint: disable=no-name-in-module, import-error
from setuptools import setup, find_packages

NAME = 'django-memdb'
DESCRIPTION = 'Django Memory Database'
VERSION = '0.0.5'
AUTHOR = 'Martin P. Hellwig'
AUTHOR_EMAIL = 'martin.hellwig@gmail.com'
URL_MAIN = "https://bitbucket.org/hellwig/" + NAME + '/'
URL_DOWNLOAD = URL_MAIN + 'download/' + VERSION + '.zip'

KEYWORDS = [
    'django',
    'django-integrator'
    ]

CLASSIFIERS = [
    'Programming Language :: Python :: 3',
    ]

REQUIREMENTS = [
    'Django',
    'django-integrator',
    'django-query-signals',
    ]

LICENSE = 'BSD'

################################################################################

KWARGS = {
    'name':NAME, 'packages':find_packages(), 'version':VERSION,
    'description':DESCRIPTION, 'author':AUTHOR, 'author_email':AUTHOR_EMAIL,
    'url':URL_MAIN, 'download_url':URL_DOWNLOAD, 'keywords':KEYWORDS,
    'license':LICENSE, 'classifiers':CLASSIFIERS,
    'install_requires':REQUIREMENTS}

setup(**KWARGS)
