#!/usr/bin/env python3

import sys, requests
from setuptools import setup, find_packages

setup(
    name='pyreconexsploit',
    version='0.0.3.5',
    author='Akuto Sai',
    description='Recon & Explitation Framework',
    long_description="""# Installation Instructions:



In order to use `search` command you must install the searchsploit binary! from {https://www.exploit-db.com/searchsploit/#install}

## Building 
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install exploitdb netcat nmap perl php
pip3 install babysploit
git clone https://github.com/AkutoSai/PyReconExSploit
cd PyReconExSploit/
python3 setup.py install
pyreconexsploit
```

# Getting Started:

#### Setting Configuration Values:

PyReconExSploit uses ConfigParser in order to write and read configuration. Your config file is automatically
generated and located at `./babysploit/config/config.cfg`. You can manually change configuration settings
by opening up the file and editing with a text editor or you can use the set command to set a new value for
a key. Use the set command like so:
```
set rhost
>> Enter Value For rhost: 10
>> Config Key Saved!
```

If before running this command the rhost key had a value of 80, the rhost key after running this command has a
value of 10. You can also add configuration variables to the config by using the set command with a new key after it
like so:
```
set newkey
>> Enter Value For newkey: hello
>> Config Key Saved!
```

Before running this there was no key named "newkey". After running this you will have a key named "newkey" in your config
until you use the `reset` command which resets the saved configuration.

#### Running A Tool

In order to run a tool all you have to do is enter the name of the tool into pyreconexsploit. You can use the `tools` command
to display a menu with all the currently available tools.

""",
    long_description_content_type='text/markdown',
    url='',
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
