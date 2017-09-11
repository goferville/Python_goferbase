import sys, threading, time, serial
from PyQt5 import QtGui, uic, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from QtEventGui import Ui_MainWindow #import ui.py ,_ .ui <- Qt Designer
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class MyWindow(QMainWindow, Ui_MainWindow): #inherite Ui_MainWindow from ui.py
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self) #get all the setup from ui.py, internal
        self.assignWedget() #remember to connect buttons, etc. to function/actions here
        self.show()

    def assignWedget(self): #connect buttons, etc. to function/actions here
        # self.pushButton.clicked.connect(self.showMsg)

        self.cB.addItems([str(x) for x in range(5)])
        self.cB.currentIndexChanged.connect(updateCbChange)
        pass
class emitTestClass(QObject):
    """
    define a customized signal: sig1
    send the signal at sendSig()
    connect sig1 to to slots
    """
    sig1=pyqtSignal() # define customized signal
    def __init__(self):
        super(emitTestClass, self).__init__()

        self.sig1.connect(processSig)
        self.sig1.connect(processSig2)
        self.sendSig()
    def sendSig(self):
        self.sig1.emit()
    def subscribeListner(self,listner):
        self.sig1.connect(listner)

def processSig():
    win .tB.append('Signal sent!')
def processSig2():
    win .tB.append('Signal sent 2!')

def processSig3():
    win .tB.append('Signal sent 3!')
def test():
    win.tB.append('Signal emitted!')
def addColorText(aText, aColor,aSize):
    aText='<span style=\" font-size:'+str(aSize)+'pt; font-weight:100; color:#ff0000;\" >'\
          +aText+ '</span>'
    win.tB.append(aText)
def updateCbChange():
    win.tB.append(win.cB.currentText())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    emt1=emitTestClass()
    emt1.subscribeListner(processSig3)
    emt1.sendSig()
    win.pbStart.setStyleSheet('QPushButton {background-color: #A3C1DA; color: grey;}')

    addColorText('I am a gofer',12,8)
    for count in range(win.cB.count()):

        win.tB.append(win.cB.itemText(count))
    win.tB.append(win.cB.currentText())
    sys.exit(app.exec_())