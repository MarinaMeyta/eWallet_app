# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/create_PIN.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_createPinDialog(object):
    def setupUi(self, createPinDialog):
        createPinDialog.setObjectName("createPinDialog")
        createPinDialog.resize(264, 147)
        self.createPinBtns = QtWidgets.QDialogButtonBox(createPinDialog)
        self.createPinBtns.setGeometry(QtCore.QRect(30, 90, 181, 32))
        self.createPinBtns.setOrientation(QtCore.Qt.Horizontal)
        self.createPinBtns.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.createPinBtns.setObjectName("createPinBtns")
        self.createPinInput = QtWidgets.QLineEdit(createPinDialog)
        self.createPinInput.setGeometry(QtCore.QRect(20, 50, 211, 27))
        self.createPinInput.setObjectName("createPinInput")
        self.label = QtWidgets.QLabel(createPinDialog)
        self.label.setGeometry(QtCore.QRect(70, 20, 131, 17))
        self.label.setObjectName("label")

        self.retranslateUi(createPinDialog)
        self.createPinBtns.accepted.connect(createPinDialog.accept)
        self.createPinBtns.rejected.connect(createPinDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(createPinDialog)

    def retranslateUi(self, createPinDialog):
        _translate = QtCore.QCoreApplication.translate
        createPinDialog.setWindowTitle(_translate("createPinDialog", "Создание PIN"))
        self.label.setText(_translate("createPinDialog", "Введите новый PIN:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createPinDialog = QtWidgets.QDialog()
    ui = Ui_createPinDialog()
    ui.setupUi(createPinDialog)
    createPinDialog.show()
    sys.exit(app.exec_())

