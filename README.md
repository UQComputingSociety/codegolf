UQCS CodeGolf Website
=====================

Linux: ![travis build status](https://travis-ci.org/UQComputingSociety/codegolf.svg?branch=master)

Windows: ![appveyor-build-status](https://ci.appveyor.com/api/projects/status/github/UQComputingSociety/codegolf?branch=master&svg=true)

This is a repository for the website for the codegolf puzzles at UQCS.

## Requirements

* Python 3.4.0+
    * Virtualenv
    * Flask
    * Flask-OAuthlib
    * Flask-Login
    * Jinja2
    * Markdown
    * pytest
    * pylint
    * Sphinx
    * sqlalchemy

* SQLLite

* The three environment variables for the Github Oauth (more details below)

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


## Github Authorisation

Hello there local developer, wondering why you cant login? well head over to the developer section on 
github and go create a developer key. An example of what to register is listed below.

Application name: codegolf local
Homepage URL: http://localhost:9000
Application Description: ""
Authorization callback URL: http://localhost:9000/user/authorize

Its then the devs reponsability to setup these enviroment variables

* 'CODEGOLF_GITHUB_CONSUMER_KEY' which is the github client id
* 'CODEGOLF_GITHUB_CONSUMER_SECRET' which is the github client secret
* 'CODEGOLF_SECRET_KEY' which is a random selection of characters

Also, when developing locally you need to set `app.testing = True`, make sure it is `False` when committing to Github. 
This value is able to be set inside `codegolf/__init__.py`