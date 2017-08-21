#!/bin/bash

pyuic5 -x ui/main_window.ui -o core/main_window.py
pyuic5 -x ui/create_PIN.ui -o core/create_pin.py
pyuic5 -x ui/enter_PIN.ui -o core/enter_pin.py
pyuic5 -x ui/remittance.ui -o core/remittance.py
pyuic5 -x ui/pyqtdesigner_test.ui -o core/test.py
