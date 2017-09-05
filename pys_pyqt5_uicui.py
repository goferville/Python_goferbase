"""
Python Gui design flow
2018/09/04
Python Gui design flow using PyQt5 + QT designer
1. Design GUI using QT designer, save as XYZ.ui;
2. Using uic to convert XYZ.ui to XYZ.Py;
3. using the format in this file to import XYZ.py/GUI ans use it;
4. Define all UI element functions in assignWedge();
5. Define all slots
"""

import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ser_ui_1 import Ui_MainWindow #import ui.py ,_ .ui <- Qt Designer

class MyWindow(QMainWindow, Ui_MainWindow): #inherite Ui_MainWindow from ui.py
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self) #get all the setup from ui.py
        self.assignWedget() #remember to connect buttons, etc. to function/actions here
        self.show()

    def assignWedget(self): #connect buttons, etc. to function/actions here
        self.pushButton.clicked.connect(self.showMsg)

    def showMsg(self): # The slot
        self.str=self.lineEdit.text() # how to reference an object
        self.lineEdit.setText('')
        if str != '':
            self.textBrowser_2.append(self.str)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())

