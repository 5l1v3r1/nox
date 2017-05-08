from setuptools import setup, find_packages
from codecs import open
from os import path
# SETUP.PY by Coco de Vienne
# Install script for *NIX systems and Windows
# licensed under the DVF GPL
setup(
    name='enigma',
    version='2017.0',
    description='file search engine',
    long_description='file search engine',
    url='http://github.com/cocodevienne/enigma',
    author='cocodevienne',
    author_email='cocodevienneoffice@gmail.com',
    license='GPLv3',
    entry_points={
        'console_scripts':[
            'enigma = enigma.__main__:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='search-engine',
    packages=find_packages(),
    install_requires=['pip', 'colorama'],
)
