# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 70, 741, 311))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 741, 281))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 739, 279))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.incomeTableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_3)
        self.incomeTableWidget.setGeometry(QtCore.QRect(0, 0, 741, 281))
        self.incomeTableWidget.setObjectName("incomeTableWidget")
        self.incomeTableWidget.setColumnCount(0)
        self.incomeTableWidget.setRowCount(0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 61, 17))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.export_wallet = QtWidgets.QAction(MainWindow)
        self.export_wallet.setObjectName("export_wallet")
        self.remit = QtWidgets.QAction(MainWindow)
        self.remit.setObjectName("remit")
        self.about = QtWidgets.QAction(MainWindow)
        self.about.setObjectName("about")
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.import_wallet = QtWidgets.QAction(MainWindow)
        self.import_wallet.setObjectName("import_wallet")
        self.menu.addAction(self.remit)
        self.menu.addAction(self.import_wallet)
        self.menu.addAction(self.export_wallet)
        self.menu.addAction(self.exit)
        self.menu_2.addAction(self.about)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Электронный кошелек"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Входящие переводы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Исходящие переводы"))
        self.label.setText(_translate("MainWindow", "Доступно:"))
        self.menu.setTitle(_translate("MainWindow", "Действия"))
        self.menu_2.setTitle(_translate("MainWindow", "Помощь"))
        self.export_wallet.setText(_translate("MainWindow", "Экспорт..."))
        self.remit.setText(_translate("MainWindow", "Перевести средства..."))
        self.about.setText(_translate("MainWindow", "О программе..."))
        self.exit.setText(_translate("MainWindow", "Выход"))
        self.import_wallet.setText(_translate("MainWindow", "Импорт..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

