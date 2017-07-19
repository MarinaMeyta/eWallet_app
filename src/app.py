import sys
from PyQt5 import QtCore, QtWidgets
from main_window import *

# replace 'c:/test.ui' with real path to ui-file created in QtDesigner
#uifile = 'c:/test.ui'
#form, base = uic.loadUiType(uifile)


class mainQtWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    myapp = mainQtWindow()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
