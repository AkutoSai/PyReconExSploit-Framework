#!/usr/bin/env python3

import sys, requests
from setuptools import setup, find_packages

setup(
    name='pyreconexsploit',
    version='0.0.3.5',
    author='Akuto Sai',
    description='Recon & Explitation Framework',
    long_description_content_type='text/markdown',
    url='https://github.com/AkutoSai/PyReconExSploit',
    packages=['pyreconexsploit'],
    install_requires=[
        'netifaces',
        'urllib3',
        'humanfriendly',
        'terminaltables',
        'pyfiglet',
        'requests',
        'raccoon-scanner'
    ],
    
    license='GNU General Public License v3 (GPLv3) (GPL)',
    zip_safe=True,
    entry_points={
        'console_scripts':[
            'pyreconexsploit = pyreconexsploit.__main__:main',
        ],
    },
    tests_require=[
        'mock;python_version<"3"',
        'pytest',
        'pytest-cov'
    ],
    classifiers=[  # Used by PyPI to classify the project and make it searchable
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: Jython',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ]
)
