#!/usr/bin/env bash

# Install Requirements
apt-get update
apt-get -y install python3-pip pylint

# Install python requirements
pip3 install -r "/vagrant/requirements.txt"