import sys
import uuid
import settings
from PyQt5 import QtCore, QtWidgets, QtGui, QtSql
from main_window import *
from remittance import *
from enter_pin import *

from wallet_token import Token
from rsa_key import RSAkey

import logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)


class userWallet():
    def __init__(self, parent=None):
        self.id = self.generateId()

    def generateId(self):
        return uuid.uuid4().hex


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
        self.ui.enterPinInput.setEchoMode(QtWidgets.QLineEdit.Password)

    def accept(self):
        print("accepted")
        self.done(QtWidgets.QDialog.Accepted)

    def reject(self):
        print("rejected")
        self.done(QtWidgets.QDialog.Rejected)



class remitDialog(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_remitDialog()
        self.ui.setupUi(self)
        self.ui.recipientIdInput.setAlignment(QtCore.Qt.AlignLeft)
        self.ui.recipientIdInput.setText("")
        self.ui.recipientIdInput.setInputMask("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        self.ui.recipientIdInput.setCursorPosition(0)

        # TODO: use validators intstead of masks
        self.ui.remitSumInput.setText("")
        self.ui.remitSumInput.setCursorPosition(0)
        self.ui.remitSumInput.setInputMask("999999")
        self.ui.remitSumInput.setCursorPosition(0)

        self.ui.remitBtn.clicked.connect(self.remit)

    def remit(self):
        recipient_id = self.ui.recipientIdInput.text()
        remitted_sum = self.ui.remitSumInput.text()
        print(recipient_id)
        print(remitted_sum)


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
        self.ui.remit.triggered.connect(self.get_remit_dialog)
        self.ui.about.triggered.connect(self.about)

    def exportWallet(self):
        self.mythread.start()
        self.exportDialog.exec()

    def on_export_finished(self):
        print("thread finished")

    def get_remit_dialog(self):
        self.remitDialog.exec()

    def showEnterPinDialog(self):
        self.enterPinDialog.exec()

    def about(self):
        QtGui.QMessageBox.about(mainWindow, "О программе", "Программа представляет собой электронный кошелек...")


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = mainWindow()
    win.show()

    win.showEnterPinDialog()

    # timer = QtCore.QTimer();
    # timer.timeout.connect(win.showEnterPinDialog)
    # timer.start(10)

    PIN = win.enterPinDialog.ui.enterPinInput.text()
    token = Token(PIN, settings.PATH_TO_TOKEN)
    rsa_key = RSAkey(PIN, settings.PATH_TO_KEY)
    if token.check_PIN(PIN) and rsa_key.key:
        logging.info("PIN is correct")
        pass
    else:
        # try entering pin again
        pass


    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
