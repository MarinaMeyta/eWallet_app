#!/bin/bash

pyuic5 -x ui/main_window.ui -o src/main_window.py
pyuic5 -x ui/create_PIN.ui -o src/create_pin.py
pyuic5 -x ui/enter_PIN.ui -o src/enter_pin.py
pyuic5 -x ui/remittance.ui -o src/remittance.py
pyuic5 -x ui/pyqtdesigner_test.ui -o src/test.py
