UQCS CodeGolf Website
=====================

![travis build status](https://travis-ci.org/UQComputingSociety/codegolf.svg?branch=master)

This is a repository for the website for the codegolf puzzles at UQCS.

## Requirements

* Python 3.4.0+
    * Virtualenv
    * Flask
    * Jinja2
    * Markdown
    * pytest
    * pylint
    * Sphinx
    * sqlalchemy

* SQLLite

## Developement Guide

To aid in setting up a development enviroment a Vagrant config has been provided as well as manual instructions.

### Vagrant Setup

When having vagrant installed just run `vagrant up` and `vagrant ssh` to get a ssh terminal of the virtual machine.
Following ports have been forwarded for access in the hosts webbrowser: (tcp: 5000)

### Manual Setup

#### Windows (with Cygwin)

0. Install python 3.4+ and navigate to project directory
1. `pip3 install virtualenv`
2. `source venv/Scripts/activate`
3. `pip3 install -r requirements.txt`
4. Start with `python3 runserver.py`

## Building Docs

Change directories into the docs folder and run `make html` to build the html sources, `make latexpdf` can also be run if
you have a latex distribution installed.

## Running Server

`python3 createDB.py`
`python3 runserver.py`
