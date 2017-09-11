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

import sys, threading, time, serial
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
        self.pushButton_2.clicked.connect(self.serStop)

    def showMsg(self): # The slot
        self.str=self.lineEdit.text() # how to reference an object
        self.lineEdit.setText('')
        if str != '':
            self.textBrowser_2.append(self.str)
    def serStop(self): # another slot
        global  serStop
        serStop=True


class SummingThread(threading.Thread):
    def __init__(self, low, high, win):
        super(SummingThread, self).__init__()
        self.low = low
        self.high = high
        self.total = 0
        self.win=win

    def run(self):
        for i in range(self.low, self.high):
            time.sleep(1)
            #self.total += i
            self.win.lcdNumber.display(i)

class SerThread(threading.Thread):
    def __init__(self, win):
        super(SerThread, self).__init__()
        self.win=win
        # initialization and open the port

        # possible timeout values:
        #    1. None: wait forever, block call
        #    2. 0: non-blocking mode, return immediately
        #    3. x, x is bigger than 0, float allowed, timeout block call

        self.ser = serial.Serial()
        # ser.port = "COM3"
        self.ser.port = "COM3"
        # ser.port = "/dev/ttyS2"
        self.ser.baudrate = 9600
        self.ser.bytesize = serial.EIGHTBITS  # number of bits per bytes
        self.ser.parity = serial.PARITY_NONE  # set parity check: no parity
        self.ser.stopbits = serial.STOPBITS_ONE  # number of stop bits
        # ser.timeout = None          #block read
        self.ser.timeout = 1  # non-block read
        # ser.timeout = 2              #timeout block read
        self.ser.xonxoff = True  # disable software flow control
        self.ser.rtscts = False  # disable hardware (RTS/CTS) flow control
        self.ser.dsrdtr = False  # disable hardware (DSR/DTR) flow control
        self.ser.writeTimeout = 2  # timeout for write
        if self.ser.is_open:
            self.ser.close()
        self.ser.open()
        self.ser.flushInput() #flush input buffer, discarding all its contents
        self.ser.flushOutput()#flush output buffer, aborting current output
                 #and discard all that is in buffer
        #try:
            #self.ser.open()
        #except Exception, e:
            #print
            #"error open serial port: " + str(e)
            #exit()

    def run(self):
        global serStop
        while True:
            time.sleep(0.1)
            if serStop:
                self.ser.close()
                break
            if self.ser.in_waiting:
                self.rx=self.ser.readline()
                self.win.textBrowser_2.append(str(self.rx))
serStop = False
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    t1=SerThread(window)
    t2=SummingThread(0,100,window)
    t1.start()
    t2.start()
    sys.exit(app.exec_())

