#!/bin/bash

# Install PyQt5, Qt designer for Python3:
sudo apt-get install python3-pyqt5
sudo apt-get install qttools5-dev-tools
sudo apt install pyqt5-dev-tools

# Qt designer binary can be found in:
# /usr/lib/x86_64-linux-gnu/qt5/bin/designer

# To convert QtDesigner ui into python code use pyuic5:
# pyuic5 -x pyqtdesigner_test.ui -o test.py

# Use pyqtdeploy for your Qt app deployment
# pip3 install pyqtdeploy

# Install QtSql dependency
sudo apt-get install python3-pyqt5.qtsql

# PyCrypto library for AES-256 usage
pip3 install pycrypto
