"""
working example 20181007
matplotlib.finance was removed and became mpl_finance

python setup.py install
"""
import datetime
import numpy as np
import matplotlib.colors as colors

import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import pandas as pd
from matplotlib.dates import date2num
import goferlib.ggf as ggf
import talib as ta

# import matplotlib.finance as finance
from mpl_finance import candlestick_ohlc


def parse_dates(x):
    return pd.to_datetime(x)


startdate = datetime.date(2001, 10, 8)
today = enddate = datetime.date.today()
enddate = datetime.date(2018, 10, 8)
ticker = 'INTC'



stockFile=ticker+'.csv'

#ggf.getGoogHistDayData2Csv(ticker, startDate, endDate, stockFile)
df=pd.read_csv(stockFile, parse_dates=['Date'],date_parser=parse_dates)
na=np.array(df.values)

print('r0=')
na[:,0]=date2num(na[:,0])
print(na[0,:])

#r=na[:,0:5]
r=na[:,[0,1,2,3,4]] #slice np array, select columns to keep, here =0,1,2,3
print("r=")
print(r[0,:])
f1, ax = plt.subplots(figsize = (10,5))

# plot the candlesticks
candlestick_ohlc(ax, r, width=.6, colorup='green', colordown='red')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.show()
