# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'web1.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 794)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tbS = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbS.setGeometry(QtCore.QRect(50, 130, 451, 401))
        self.tbS.setObjectName("tbS")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 100, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 100, 47, 13))
        self.label_2.setObjectName("label_2")
        self.tbC = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbC.setGeometry(QtCore.QRect(540, 130, 451, 401))
        self.tbC.setObjectName("tbC")
        self.pb1 = QtWidgets.QPushButton(self.centralwidget)
        self.pb1.setGeometry(QtCore.QRect(590, 560, 75, 23))
        self.pb1.setObjectName("pb1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1070, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Server"))
        self.label_2.setText(_translate("MainWindow", "Client"))
        self.pb1.setText(_translate("MainWindow", "Connect"))

