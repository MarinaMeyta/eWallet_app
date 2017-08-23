#!/bin/bash

# Qt designer binary can be found in:
# /usr/lib/x86_64-linux-gnu/qt5/bin/designer

# To convert QtDesigner ui into python code use pyuic5:
# pyuic5 -x pyqtdesigner_test.ui -o test.py

# run pytest without import errors
python -m pytest -v tests/