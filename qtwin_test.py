from data_label.pyqtgraph.pyqtgraph_testwin import Ui_MainWindow
import sys, datetime, time, threading, math
import serial, visa
from PyQt5 import QtGui, QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
import numpy as np
import  pyqtgraph as pg
class MyWindow(QMainWindow, Ui_MainWindow):  # inherite Ui_MainWindow from ui.py

    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)  # get all the setup from ui.py

        #uic.loadUi('pyqtgraph_testwin.ui', self)

        self.init_Widget()

        self.show()
        # self.setupPar() # serial port parameter
        # self.t1 = threading.Thread(target=self.server1)
        # self.t1.start()
    def init_Widget(self):
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        #p=self.graphicsView.plot(hour, temperature)# graphicsView here is a qtgraph plotWidge after promotion

        self.item = CandlestickItem(data)
        self.plt = self.graphicsView.addItem(self.item)
        #self.plt.addItem(self.item)
        self.plot=self.graphicsView.getPlotItem()
        self.graphicsView.scene().sigMouseMoved.connect(self.mouse)
    def mouse(self,ev):
        print(ev.x(),ev.y())
        mousepos = np.array([ev.x(), ev.y()])
        qpos=self.plot.vb.mapSceneToView(ev)
        print(qpos.x(), qpos.y())


class CandlestickItem(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data  ## data must have fields: time, open, close, min, max
        self.generatePicture()

    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)

        w = (self.data[1][0] - self.data[0][0]) / 3.31
        for (t, open, close, min, max) in self.data:
            p.setPen(pg.mkPen('w'))
            p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            if open > close:
                p.setBrush(pg.mkBrush('r'))
                p.setPen(pg.mkPen('r'))
            else:
                p.setBrush(pg.mkBrush('g'))
                p.setPen(pg.mkPen('g'))
            p.drawRect(QtCore.QRectF(t - w, open, w * 2, close - open))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())

data = [  ## fields are (time, open, close, min, max).
    [1., 10, 13, 5, 15],
    [2., 13, 17, 9, 20],
    [3., 17, 14, 11, 23],
    [4., 14, 15, 5, 19],
    [5., 15, 9, 8, 22],
    [6., 9, 15, 8, 16],
    [7., 12, 18, 8.5, 22]]

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = MyWindow()

    sys.exit(app.exec_())

'''
https://pyqtgraph.readthedocs.io/en/latest/how_to_use.html
Embedding widgets inside PyQt applications
For the serious application developer, all of the functionality in pyqtgraph is available via widgets 
that can be embedded just like any other Qt widgets. Most importantly, see: PlotWidget, ImageView, 
GraphicsLayoutWidget, and GraphicsView. PyQtGraph’s widgets can be included in Designer’s ui files 
via the “Promote To…” functionality:

In Designer, create a QGraphicsView widget (“Graphics View” under the “Display Widgets” category).
Right-click on the QGraphicsView and select “Promote To…”.
Under “Promoted class name”, enter the class name you wish to use (“PlotWidget”, “GraphicsLayoutWidget”, etc).
Under “Header file”, enter “pyqtgraph”.
Click “Add”, then click “Promote”.
See the designer documentation for more information on promoting widgets. The “VideoSpeedTest” and 
“ScatterPlotSpeedTest” examples both demonstrate the use of .ui files that are compiled to .py modules 
using pyuic4 or pyside-uic. The “designerExample” example demonstrates dynamically generating python 
classes from .ui files (no pyuic4 / pyside-uic needed).

'''
