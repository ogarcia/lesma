#!/usr/bin/env python

import lesma as project

from setuptools import setup
from setuptools import find_packages
from pip.req import parse_requirements
from pip.download import PipSession


def get_file_content(fname):
    try:
        return open(fname).read()
    except:
        return None


setup(
    name=project.NAME,
    version=project.VERSION,
    description=project.DESCRIPTION,
    long_description=get_file_content('README.md'),
    author=project.AUTHOR_NAME,
    author_email=project.AUTHOR_EMAIL,
    url=project.URL,
    packages=find_packages(),
    install_requires=[str(x.req) for x in
                      parse_requirements('requirements.txt',
                      session=PipSession())],
    package_data={
        'lesma': [
            'app/static/css/*',
            'app/static/help/*',
            'app/static/img/*',
            'app/static/js/*',
            'app/templates/*'
            ]
    },
    license=project.LICENSE,
    entry_points={
        'console_scripts': [
            'lesma = lesma.main:cli',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],

    test_suite="tests.suite",
    include_package_data=True,
)
