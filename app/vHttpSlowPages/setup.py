import os
from setuptools import setup, find_packages
import vHttpSlowPages

Name = 'vHttpSlowPages'
Version = vHttpSlowPages.__version__

setup(
    name = Name,
    version = Version,
    packages = [Name],
    author = 'VladVons',
    author_email = 'vladvons@gmail.com',
    url = 'https://github.com',
    python_requires = ">=3.7",
    description = 'A simple web scraper to detect slow pages',
    keywords = 'async http scraper slow pages',
    license = 'freeware',
    install_requires = [
        'asyncio', 'aiohttp', 'aiohttp-socks', 'lxml', 'bs4'
    ],
    entry_points = {
        'console_scripts': [
            '%s = %s.%s:Main' % (Name, Name, Name)
        ]
    },
    #package_data= {
    #    Name: ['*.json', '*.sh']
    #}
)
