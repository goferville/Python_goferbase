from data_label.pyqtgraph.pg_ui import Ui_MainWindow
import sys, time, threading, math
import serial, visa
from PyQt5 import QtGui, QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
import numpy as np
import pyqtgraph as pg
from datetime import datetime, timezone, timedelta
import pandas as pd

import jet.etlib.mysql_lib as sqllib

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
        # self.graphicsView = GraphicsLayoutWidget
        #pg.setConfigOption('background', (20, 28, 38))
        self.plot = self.graphicsView.addPlot(row=0, col=0)

        self.plotVol=self.graphicsView.addPlot(row=1, col=0)
        self.plotAcct = self.graphicsView.addPlot(row=2, col=0)

        self.plotVol.showGrid(x=True, y=True, alpha=0.3)
        self.plotAcct.showGrid(x=True, y=True, alpha=0.3)
        self.plotVol.setXLink(self.plot)
        self.plotAcct.setXLink(self.plot)

        self.graphicsView.ci.layout.setRowStretchFactor(0, 4)
        self.graphicsView.ci.layout.setRowStretchFactor(1, 1)
        self.graphicsView.ci.layout.setRowStretchFactor(2, 1)
        self.plot_chart()
        #self.buysell=BuySellItem(data)

        #self.plt.addItem(self.item)
        #self.plot=self.vCandle.getPlotItem()


        #self.graphicsView.setBackground('w')
        self.graphicsView.setBackground(candleBackground)
        #self.plot.vb.setBackgroundColor(candleBackground)
        #self.plotVol.vb.setBackgroundColor(candleBackground)
        #self.plotAcct.vb.setBackgroundColor(candleBackground)
        self.plot.showGrid(x=True, y=True, alpha = 1.0)
        self.vb_plot=self.plot.vb
        #direct connect
        #self.graphicsView.scene().sigMouseMoved.connect(self.mouseMoved) #for whole plotWidget

        # indirect connect - using a proxy
        #self.plot.scene().sigMouseMoved.connect(self.mouseMoved) #use follwoing proxy to convert ev to connect
        #using signal proxy turns original arguments into a tuple
        self.proxy = pg.SignalProxy(self.plot.scene().sigMouseMoved, rateLimit=120, slot=self.mouseMoved)
        self.set_mouse_crosshair()


        self.plot_acct()
    def mouseMoved(self,ev):
        #print(ev.x(),ev.y())
        pos=ev[0]
        #pos = [ev.x(), ev.y()]
        if self.vb_plot.sceneBoundingRect().contains(pos):
            qpos = self.plot.vb.mapSceneToView(pos)
            self.mvLine.setPos(qpos.x())
            self.mhLine.setPos(qpos.y())

            # v line for volume plot
            self.mvLineVol.setPos(qpos.x())

            # v line for account plot
            self.mvLineAcct.setPos(qpos.x())


    def plot_chart(self):
        axis = pg.DateAxisItem()
        self.plot.setAxisItems({'bottom': axis})
        chartf, tradef = ohlcFromDatabase('esu0')
        (drow,dcol)=chartf.shape
        data_time=np.zeros((drow,1))
        raw_time=chartf.index
        data_volume = np.zeros((drow, 1))
        data_ohlc=chartf.values[:,:-1] # np.zeros((chartf.size,4))

        #To read time (a time stamp obj) from SQL then convert to integer
        for i in range(drow):
            #summer time change, need to change timedelta(hours=7) or hours=6
            #for both chart & trade plot
            data_time[i][0]=(raw_time[i] + timedelta(hours=7)).replace(tzinfo=timezone.utc).timestamp()
        candle_data=np.concatenate((data_time,data_ohlc), axis=1)
        data_vol_1d=(chartf.values[:,4:]).reshape((drow,))
        date_time_1d=data_time.reshape((drow,))
        #data_vol_1d = (chartf.values[:, 4:])
        #date_time_1d = data_time

        self.candle = CandlestickItem(candle_data)
        self.plt = self.plot.addItem(self.candle)
        ax0 = self.plot.getAxis('bottom')
        # self.plot.showGrid(x=True, y=True, alpha=1.0)
        ax0.setStyle(showValues=True)  # False = invisible
        self.plot.showGrid(x=True, y=True, alpha=0.3)
        self.volBarColor=np.zeros(drow)
        for i in range(drow):
            if candle_data[i][3]>=candle_data[i][0]:
                #self.volBarColor[i]=candleGreen
                self.volBarColor[i] =1
            else:
                #self.volBarColor[i] = candleRed
                self.volBarColor[i] = 0
        self.plot_vol(date_time_1d, data_vol_1d)
        self.plot_trade(tradef)

    def plot_acct(self):
        #axis = pg.DateAxisItem()
        #self.plotAcct.setAxisItems({'bottom': axis})
        # region directly plot scatter buysell
        pass
        sx, sy = generateTradingData()
        #self.plot.plot(sx, sy, pen=None, symbol='o')
        # pen is for conencting line
        #self.plot.plot(sx, sy, size = 35,pen=(0, 0, 200), symbolBrush=(0, 0, 200), symbolPen='w', symbol='o')
        # endregion directly plot scatter buysell

    def plot_vol(self, sx,sy):
        axis = pg.DateAxisItem()
        self.plotVol.setAxisItems({'bottom': axis})
        self.bg1 = pg.BarGraphItem(x=sx, height=sy, width=5)
        self.plotVol.addItem(self.bg1)
        '''
        #self.plotVol.plot(sx, sy, size=35, pen=(0, 0, 200), symbolBrush=(0, 0, 200), symbolPen='w', symbol='o')
        for i in range(len(self.volBarColor)):
            if self.volBarColor[i]==1:
                barColor=candleGreen
            else:
                barColor=candleRed
            barItem= pg.BarGraphItem(x=sx[i], height=sy[i], width=5, brush=barColor, pen=barColor)
            self.plotVol.addItem(barItem)
        '''
    def plot_trade(self, trade_df):
        for i in range(4):
            self.plot_trade_option(trade_df,str(i+1))


    def plot_trade_option(self, trade_df,option='1'):
        brush =[(0,200,0), (0,0,200), (0,125,0), (0,0,125)]
        symbolId = trade_df['action'] == option
        # symbolIdBuy = trade_df['action'] == '1'
        # get buy dat and time index
        trade_data_df = trade_df[symbolId]
        (drow, dcol) = trade_data_df.shape
        if drow !=0:
            y = trade_data_df.values[:, 4]
            x = np.zeros(drow)
            raw_time = trade_data_df.index + timedelta(hours=7)
            for i in range(drow):
                x[i] = raw_time[i].replace(tzinfo=timezone.utc).timestamp()
                #x[i] = raw_time[i].timestamp()+timedelta(hours=7)
                qtyText=pg.TextItem(text=str(trade_df['quantity'][i]))
                qtyText.setPos(x[i],y[i])
                # vb is attribute of a plotItem
                # like signalgraph = pg.PlotWidget(name='Signalgraph'); vb = signalgraph.plotItem.vb
                self.plot.vb.addItem(qtyText)
            self.plot.plot(x, y, size=35, pen=None, symbolBrush=brush[int(option)-1], symbolPen='w', symbol='o')
    def set_mouse_crosshair(self):
        self.mvLine = pg.InfiniteLine(angle=90, movable=False)
        self.mvLineVol = pg.InfiniteLine(angle=90, movable=False)
        self.mvLineAcct = pg.InfiniteLine(angle=90, movable=False)
        self.mhLine = pg.InfiniteLine(angle=0, movable=False)
        self.plot.addItem(self.mvLine, ignoreBounds=True)
        self.plot.addItem(self.mhLine, ignoreBounds=True)
        self.plotVol.addItem(self.mvLineVol, ignoreBounds=True)
        self.plotAcct.addItem(self.mvLineAcct, ignoreBounds=True)
class CandlestickItem(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data  ## data must have fields: time, open, max, min, close - ohlc
        self.generatePicture()

    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)

        candleRed=(255,98,62)
        candleGreen=(35,225,167)
        candleBackground=(20,28,38)
        candleBackgroundLine = (24,34,45)
        w = (self.data[1][0] - self.data[0][0]) / 3.31
        for (t, open, max, min, close) in self.data:
            p.setPen(pg.mkPen((110, 116, 125)))# can replace 'w' with (255,0,0)
            p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            if open > close:
                p.setBrush(pg.mkBrush(candleRed))
                p.setPen(pg.mkPen(candleRed))
            else:
                p.setBrush(pg.mkBrush(candleGreen))
                p.setPen(pg.mkPen(candleGreen))
            p.drawRect(QtCore.QRectF(t - w, open, w * 2, close - open))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())

class BuySellItem(pg.ScatterPlotItem):
    def __init__(self, x, y):
        self.bsitem=pg.ScatterPlotItem.__init__(self)
        self.x=x
        self.y=y
        self.generateItem()

    def generateItem(self):
        buysellitem=0

def generateTradingData():
    sx = np.zeros(2)
    sx[0] = data[0][0]
    sx[1] = data[1][0]
    sy = np.zeros(2)
    sy[0] = 15
    sy[1] = 18
    return sx,sy

def ohlcFromDatabase(stock):
    dbIP = '192.168.1.168'
    #stock = "bynd"
    dbName = 'koala2020'
    tbTrade = 'eTradeExecOrder'  # id, time, symbol, qty, price
    cnx, cur = sqllib.database_connection(dbName, dbIP)
    timeRange = "where time between '2020-07-20 00:00:01' and '2020-08-01 23:59:00'"
    symbolRange = f'and  symbol="{stock}"'
    # pdf=pd.read_sql(f'SELECT * FROM {dbName}.{tbTrade}', cnx, index_col=['id'],)
    tradef = pd.read_sql(f'SELECT * FROM {dbName}.{tbTrade} {timeRange} '
                         f'{symbolRange}', cnx, index_col=['time'], )
    print(tradef)
    #default chart data: 1-min data
    tbChart = stock+'_1_min'
    chartf = pd.read_sql(f'SELECT * FROM {dbName}.{tbChart} {timeRange} ',
                         cnx, index_col=['time'], )
    print(f'SELECT * FROM {dbName}.{tbChart} {timeRange} ')
    print(chartf)
    cur.close()
    cnx.close()
    return chartf, tradef
"""
data = [  ## fields are (time, open, close, min, max).
    [25536, 10, 13, 5, 15],
    [25537., 13, 17, 9, 20],
    [25538, 17, 14, 11, 23],
    [25539, 14, 15, 5, 19],
    [25540, 15, 9, 8, 22],
    [25541, 9, 15, 8, 16],
    [25542, 12, 18, 8.5, 22]]
"""
candleRed=(255,98,62)
candleGreen=(35,225,167)
data = [  ## fields are (time, open, close, min, max).
    [(datetime.strptime('07/17/2020, 03:51:03 PM', '%m/%d/%Y, %I:%M:%S %p')).replace(tzinfo=timezone.utc).timestamp(), 10, 13, 5, 15],
    [(datetime.strptime('07/17/2020, 03:53:03 PM', '%m/%d/%Y, %I:%M:%S %p')).replace(tzinfo=timezone.utc).timestamp(), 13, 17, 9, 20],]

buyselldata=[]
candleBackground = (20, 28, 38)
if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = MyWindow()

    sys.exit(app.exec_())


'''
Setting Axis Limits

self.graphWidget.setXRange(5, 20, padding=0)
self.graphWidget.setYRange(30, 40, padding=0)
Legends
self.graphWidget.plot(hour, temperature, name = "Sensor 1",  pen = NewPen, symbol='+', symbolSize=30, symbolBrush=('b'))
self.graphWidget.addLegend()

self.graphWidget.showGrid(x=True, y=True)

self.graphWidget.clear()

Update Line

self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)
self.data_line.setData(self.x, self.y)

example of update:

    def update_plot_data(self):

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first 
        self.y.append( randint(0,100))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.

'''
