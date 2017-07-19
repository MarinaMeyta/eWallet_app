# Infotechs Test Task

1. Install PyQt5, Qt designer for Python3:
sudo apt-get install python3-pyqt5
sudo apt-get install qttools5-dev-tools
sudo apt install pyqt5-dev-tools

Qt designer binary can be found in:
/usr/lib/x86_64-linux-gnu/qt5/bin/designer

2. To convert QtDesigner ui into python code use pyuic5:
pyuic5 -x pyqtdesigner_test.ui -o test.py

3. Use pyqtdeploy for your Qt app deployment
pip3 install pyqtdeploy

4. Install QtSql dependency
sudo apt-get install python3-pyqt5.qtsql

