"""
GogleFinanceTest.csv
"""
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import pandas as pd

import datetime as dt
from matplotlib.dates import date2num
from matplotlib.dates import DateFormatter, WeekdayLocator,\
    DayLocator, MONDAY
import goferlib.goferGoogleFinance as ggf
import requests, io
# 1

#dtypes = [datetime, float, float, float,float, int]
#parse_dates = date2num(['Date'])
#df=pd.read_csv("GogleFinanceTest.csv")
# 2
# parse_dates = date2num(pd.to_datetime(['Date']))
def parse_dates(x):
    return (pd.to_datetime(x))


startDate=dt.datetime(2016,3,12)
endDate=dt.datetime.now()
ggf.getGoogHistDayData2Csv('AMD', startDate, endDate,"testIntc.csv")
df=pd.read_csv("testIntc.csv", parse_dates=['Date'],date_parser=parse_dates)

#df = pd.read_csv(io.StringIO(response.content.decode('utf-8')), parse_dates=['Date'],date_parser=parse_dates)

#df=ggf.getGoogHistDayData('INTC', startDate, endDate)
# df[:,0]=date2num(df[:,0])
print(df.dtypes)
na1=df.values
#na1[:,0]=date2num(pd.to_datetime(na1[:,0]))
na1[:,0]=date2num((na1[:,0]))
print(na1)
#plot data----------------------------------------
mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12


fig, ax1 = plt.subplots(1,1)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d')) #otherwise see numbers
ax1.xaxis.set_major_locator(mondays)
ax1.xaxis.set_minor_locator(alldays)
ax1.xaxis.set_major_formatter(weekFormatter)
#ax1.xaxis.set_major_formatter(weekFormatter)
ax1.xaxis.set_major_locator(mticker.MaxNLocator(21))#max x-axis labels
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)


candlestick_ohlc(ax1, na1, width=0.4, colorup='#00ff00', colordown='#ff0000')
plt.show()