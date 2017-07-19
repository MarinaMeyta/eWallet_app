# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/enter_PIN.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_enterPinDialog(object):
    def setupUi(self, enterPinDialog):
        enterPinDialog.setObjectName("enterPinDialog")
        enterPinDialog.resize(365, 153)
        self.enterPinBtns = QtWidgets.QDialogButtonBox(enterPinDialog)
        self.enterPinBtns.setGeometry(QtCore.QRect(90, 90, 181, 32))
        self.enterPinBtns.setOrientation(QtCore.Qt.Horizontal)
        self.enterPinBtns.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.enterPinBtns.setObjectName("enterPinBtns")
        self.label = QtWidgets.QLabel(enterPinDialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 321, 21))
        self.label.setObjectName("label")
        self.enterPinInput = QtWidgets.QLineEdit(enterPinDialog)
        self.enterPinInput.setGeometry(QtCore.QRect(70, 50, 231, 27))
        self.enterPinInput.setObjectName("enterPinInput")

        self.retranslateUi(enterPinDialog)
        self.enterPinBtns.accepted.connect(enterPinDialog.accept)
        self.enterPinBtns.rejected.connect(enterPinDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(enterPinDialog)

    def retranslateUi(self, enterPinDialog):
        _translate = QtCore.QCoreApplication.translate
        enterPinDialog.setWindowTitle(_translate("enterPinDialog", "Dialog"))
        self.label.setText(_translate("enterPinDialog", "Для продолжения работы с программой введите PIN:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    enterPinDialog = QtWidgets.QDialog()
    ui = Ui_enterPinDialog()
    ui.setupUi(enterPinDialog)
    enterPinDialog.show()
    sys.exit(app.exec_())

