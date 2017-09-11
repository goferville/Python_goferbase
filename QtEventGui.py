# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtEventGui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pbStart = QtWidgets.QPushButton(self.centralwidget)
        self.pbStart.setGeometry(QtCore.QRect(200, 170, 75, 23))
        self.pbStart.setObjectName("pbStart")
        self.pbStop = QtWidgets.QPushButton(self.centralwidget)
        self.pbStop.setGeometry(QtCore.QRect(200, 240, 75, 23))
        self.pbStop.setStyleSheet("background-color: rgb(255, 0, 255);\n"
"color: rgb(85, 170, 0);")
        self.pbStop.setObjectName("pbStop")
        self.tB = QtWidgets.QTextBrowser(self.centralwidget)
        self.tB.setGeometry(QtCore.QRect(320, 130, 256, 192))
        self.tB.setStyleSheet("")
        self.tB.setObjectName("tB")
        self.cB = QtWidgets.QComboBox(self.centralwidget)
        self.cB.setGeometry(QtCore.QRect(320, 340, 121, 22))
        self.cB.setObjectName("cB")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbStart.setText(_translate("MainWindow", "Start"))
        self.pbStop.setText(_translate("MainWindow", "Stop"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

