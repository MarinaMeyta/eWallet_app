# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/remittance.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_remitDialog(object):
    def setupUi(self, remitDialog):
        remitDialog.setObjectName("remitDialog")
        remitDialog.resize(412, 117)
        self.recipientIdInput = QtWidgets.QLineEdit(remitDialog)
        self.recipientIdInput.setGeometry(QtCore.QRect(130, 20, 241, 27))
        self.recipientIdInput.setObjectName("recipientIdInput")
        self.remitSumInput = QtWidgets.QLineEdit(remitDialog)
        self.remitSumInput.setGeometry(QtCore.QRect(130, 60, 111, 27))
        self.remitSumInput.setObjectName("remitSumInput")
        self.remitBtn = QtWidgets.QPushButton(remitDialog)
        self.remitBtn.setGeometry(QtCore.QRect(260, 60, 111, 27))
        self.remitBtn.setObjectName("remitBtn")
        self.label = QtWidgets.QLabel(remitDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(remitDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 101, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(remitDialog)
        QtCore.QMetaObject.connectSlotsByName(remitDialog)

    def retranslateUi(self, remitDialog):
        _translate = QtCore.QCoreApplication.translate
        remitDialog.setWindowTitle(_translate("remitDialog", "Перевод денежных средств"))
        self.remitBtn.setText(_translate("remitDialog", "Отправить"))
        self.label.setText(_translate("remitDialog", "ID получателя:"))
        self.label_2.setText(_translate("remitDialog", "Сумма перевода:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    remitDialog = QtWidgets.QDialog()
    ui = Ui_remitDialog()
    ui.setupUi(remitDialog)
    remitDialog.show()
    sys.exit(app.exec_())

