import sys
from PyQt5 import QtCore, QtWidgets, QtGui, QtSql
from main_window import *
from remittance import *
from enter_pin import *


class myThread(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        for i in range(1, 4):
            self.sleep(3) # sleep for 3 seconds
            print("i = %s" % i)


class enterPinDialog(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_enterPinDialog()
        self.ui.setupUi(self)


class remitDialog(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_remitDialog()
        self.ui.setupUi(self)


class mainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        # self.ui.remitDialog = Ui_remitDialog()
        # remitDialog = QtWidgets.QDialog()
        self.ui.setupUi(self)

        self.remitDialog = remitDialog()
        self.exportDialog = QtWidgets.QFileDialog()
        self.enterPinDialog = enterPinDialog()

        self.mythread = myThread()

        self.ui.export_wallet.triggered.connect(self.exportWallet)
        self.mythread.started.connect(self.exportWallet)
        self.mythread.finished.connect(self.on_export_finished)

        self.ui.exit.triggered.connect(QtWidgets.qApp.quit)
        self.ui.remit.triggered.connect(self.remit)

    def exportWallet(self):
        self.mythread.start()
        self.exportDialog.exec()

    def on_export_finished(self):
        print("thread finished")

    def remit(self):
        self.remitDialog.exec()

    def showEnterPinDialog(self):
        self.enterPinDialog.exec()


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = mainWindow()
    win.show()

    # timer = QtCore.QTimer();
    # timer.timeout.connect(win.showEnterPinDialog)
    # timer.start(10)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
