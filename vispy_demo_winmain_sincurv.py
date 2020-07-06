import sys, datetime, time, threading, math
import serial, visa
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from data_label.testwin import Ui_MainWindow  # import ui.py ,_ .ui <- Qt Designer
import math, socket
import vispy.app
from vispy import scene, visuals
import numpy as np

global posh, colorh, mh


class MyWindow(QMainWindow, Ui_MainWindow):  # inherite Ui_MainWindow from ui.py
    global posh, colorh

    def __init__(self):
        super(MyWindow, self).__init__()

        self.setupUi(self)  # get all the setup from ui.py
        # self.assignWedget() #remember to connect buttons, etc. to function/actions here
        # self.verticalLayout.

        # working --------
        # self.canvas = vispy.app.Canvas()
        # set parent, this is optional
        # self.canvas.create_native()
        # self.canvas.native.setParent(self)
        # working --------
        # working 2--------
        self.init_Widget()

        self.show()
        # self.setupPar() # serial port parameter
        # self.t1 = threading.Thread(target=self.server1)
        # self.t1.start()
    def init_Widget(self):
        self.canvas = scene.SceneCanvas(keys='interactive')
        self.canvas.create_native()
        self.canvas.native.setParent(self)
        self.grid = self.canvas.central_widget.add_grid(spacing=0)
        self.viewbox = self.grid.add_view(row=0, col=1, camera='panzoom')
        #self.viewbox = self.grid.add_view(row=0, col=1, camera='turntable')

        # add some axes
        self.x_axis = scene.AxisWidget(orientation='bottom')
        self.x_axis.stretch = (1, 0.1)
        self.grid.add_widget(self.x_axis, row=1, col=1)
        self.x_axis.link_view(self.viewbox)
        self.y_axis = scene.AxisWidget(orientation='left')
        self.y_axis.stretch = (0.1, 1)
        self.grid.add_widget(self.y_axis, row=0, col=0)
        self.y_axis.link_view(self.viewbox)
        self.setup_curve_data()
        self.setup_cross_data()
        self.line = scene.Line(self.pos, self.color, parent=self.viewbox.scene)

        self.lineh = scene.Line(self.posh, self.colorh, parent=self.viewbox.scene)
        self.linev = scene.Line(self.posv, self.colorh, parent=self.viewbox.scene)
        self.marker=scene.visuals.Markers()
        self.marker.set_data(pos=self.posm,symbol='o',face_color='white')
        self.viewbox.add(self.marker)
        # auto-scale to see the whole line.
        self.viewbox.camera.set_range()

        self.verticalLayout.addWidget(self.canvas.native)
        self.pushButton_3 = QtWidgets.QPushButton()
        self.verticalLayout.addWidget(self.pushButton_3)
        # self.pushButton.setGeometry(QtCore.QRect(960, 130, 112, 34))
        self.pushButton_3.setObjectName("testButton")
        self.pushButton_3.setText("Qt Button")
        # self.canvas.events.mouse_press.connect(self.press1)
        #self.b1.camera.viewbox.events.mouse_press.connect(self.press1)
        #print(self.b1.camera._scene_transform)
        self.canvas.events.mouse_move.connect(self.plot_update)
        self.canvas.events.mouse_press.connect(self.mouse_press_hdl)

    def plot_update(self, ev):
        d1 = np.array([ev.pos[0], ev.pos[1], 0, 1])
        tf1 = self.lineh.transforms.get_transform('visual', 'canvas')
        # print(tf1)
        p3 = tf1.imap(d1)
        print(p3)
        self.posh[0, 1] = p3[1]
        self.posh[1, 1] = p3[1]
        self.posh[0, 0] = p3[0] - 500
        self.posh[1, 0] = p3[0] + 500
        # print(posh)
        self.lineh.set_data(self.posh, self.colorh)
        self.posv[0, 0] = p3[0]
        self.posv[1, 0] = p3[0]
        self.posv[0, 1] = p3[1] - 500
        self.posv[1, 1] = p3[1] + 500
        # print(posv)
        self.linev.set_data(self.posv, self.colorh)

    def mouse_press_hdl(self, ev):
        print("mouse button = ", ev.button)

    def setup_curve_data(self):
        # vertex positions of data to draw
        N = 126
        self.pos = np.zeros((N, 2), dtype=np.float32)
        # x_lim = [50., 750.]
        # y_lim = [-2., 2.]
        x = np.arange(0, 4 * np.pi, 0.1)  # start,stop,step, N=126
        y = np.sin(x)
        self.pos[:, 0] = x
        self.pos[:, 1] = y
        # self.color array
        # white
        self.color = np.ones((N, 4), dtype=np.float32)
        # self.color
        self.color[:, 0] = np.linspace(0, 1, N)
        self.color[:, 1] = self.color[::-1, 0]
        M=40
        self.posm = np.zeros((M, 2), dtype=np.float32)
        xm = np.arange(0, 4 * np.pi, 0.32)  # start,stop,step, M=40
        ym = np.sin(xm)+1
        self.posm[:, 0] = xm
        self.posm[:, 1] = ym
        self.colorm = np.ones((M, 4), dtype=np.float32)
        # self.color
        self.colorm[:, 0] = np.linspace(0, 1, M)
        self.colorm[:, 1] = self.colorm[::-1, 0]
    def setup_cross_data(self):
        self.posh = np.zeros((2, 2), dtype=np.float32)
        self.posv = np.zeros((2, 2), dtype=np.float32)
        self.colorh = np.ones((2, 4), dtype=np.float32)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = MyWindow()

    sys.exit(app.exec_())
