import sys, datetime, time, threading, math
import serial, visa
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from web1 import Ui_MainWindow  # import ui.py ,_ .ui <- Qt Designer
import math, socket



class MyWindow(QMainWindow, Ui_MainWindow): #inherite Ui_MainWindow from ui.py
    #def par
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setupUi(self) #get all the setup from ui.py
        self.assignWedget() #remember to connect buttons, etc. to function/actions here
        self.show()
        self.setupPar() # serial port parameter
        self.t1 = threading.Thread(target=self.server1)
        self.t1.start()

    def assignWedget(self): #connect buttons, etc. to function/actions here
        self.pb1.clicked.connect(self.pb1_clicked)

    def pb1_clicked(self):
        self.client1()
    def setupPar(self):
        pass
    def server1(self):

        s1 = socket.socket()
        port = 12345
        s1.bind(('', port))
        s1.listen(5)
        self.tmpmsg = 'Server1 Ready!'
        self.tbS.append(self.tmpmsg)
        self.tbS.moveCursor(QtGui.QTextCursor.End)
        while True:
            c1, addr1 = s1.accept()
            #c1, addr1 = s1.recvfrom(65535)
            self.tmpmsg='Got connection {}'.format(addr1)
            self.tbS.append(self.tmpmsg)
            self.tbS.moveCursor(QtGui.QTextCursor.End)
            msg1 = ('Goferville got your connection!' + '   The time is {}'.format(datetime.datetime.now())).encode()
            c1.send(msg1)
            c1.close()
    def client1(self):
        c = socket.socket()
        portc = 12345
        c.connect(('127.0.0.1', portc))
        msg2 = (c.recv(1024)).decode()
        self.tmpmsg ='msg from server1:' + msg2

        self.tbC.append(self.tmpmsg)
        self.tbC.moveCursor(QtGui.QTextCursor.End)
        c.send('Hello from client1'.encode())

        c.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()

    sys.exit(app.exec_())