NOX
===

About
=====
Nox is a simple, yet powerful penetration-testing tool written in Python.

Usage
=====
Usage:

.. code-block:: bash

    $ # connect to a target
    $ nox --connect -IP www.google.com -port 80 -b 1024
    $ # "-b" is the size of the received answer
    
    $ # send a payload
    $ nox --pay -IP www.google.com -port 80
    
    $ # DDOS on a target
    $ nox --ddos -IP www.google.com -port 80 -bo 2000000
    $ # "-bo" is the bufferoverflow, i.e. the amount of requests that will crash a server

Required Programs
=================
The following programs should be installed on your system for Nox to work correctly:

- Python 3.4 or up
- Git 2.7 or up
- Pip 8.1 or up
- Wheel current version
- Setuptools 32.0 or up

Installation from source
========================
.. code-block:: bash

    $ git clone https://github.com/cocodevienne/nox
    $ cd source/enigma
    $ python setup.py install
    

Building
========
1.) Get the source
------------------
.. code-block:: bash

    $ git clone https://github.com/cocodevienne/nox

2.) Build the source
--------------------
.. code-block:: bash

    $ cd source/nox
    $ python setup.py bdist_wheel
    $ python setup.py sdist

3.) Test your build
-------------------
.. code-block:: bash

    $ cd dist
    $ pip install <wheel name>
    $ nox -v



Changelog
=========
.. code-block:: python

    Version 2017.0:
        - initial release
        - upload to GitHub

Licensing
=========
This software is licensed under the DVF GPL.

NOTE
====
I am not responsible for how this software is used! This IS pentesting software and how you use it I leave to you!
        
External Links
==============
- Source: https://github.com/cocodevienne/nox

COCO DE VIENNE 2017