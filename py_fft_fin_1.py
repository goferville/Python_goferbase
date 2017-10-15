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

import  numpy as np
from numpy import fft
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
ggf.getGoogHistDayData2Csv('INTC', startDate, endDate,"testIntc.csv")
df=pd.read_csv("intc.csv", parse_dates=['Date'],date_parser=parse_dates)
na=np.array(df.values)
na1=np.c_[na,na[:,4]] # add faked adj_close to google data which has already adjusted prices
#na1[:,0]=date2num(na1[:,0])

r = np.rec.fromrecords(na1, names="date,open,high,low,close,volume")
n=len(r.close)
fx=r.close
t=np.arange(0,n)
Fk=fft.fft(fx)/n
fd=1 #sample frequency
dx=1/fd
nu=fft.fftfreq(n,dx) #Natural frequencies

Fk=fft.fftshift(Fk) #Shift zero frequency to center


ctrN=int(n/2)
#=============
#filter
hPass=False

winHW=60
if hPass:
    #low pass
    Fk[ctrN-winHW:ctrN+winHW]=0
else:
    #high pass
    Fk[0:ctrN-winHW]=0
    Fk[ctrN+winHW:n]=0
#==========
nu=fft.fftshift(nu)
print(nu)
fig,ax=plt.subplots(5,1,sharex=False)
ax[0].plot(nu, np.real(Fk))
ax[1].plot(nu, np.imag(Fk))
ax[2].plot(nu, np.absolute(Fk))

fxb=fft.ifft(Fk)
if hPass:
    #low pass
    fxb[0:10]=0
    fxb[n-10:n]=0
ax[3].plot(t,np.abs(fxb)/np.abs(fxb[100]))
ax[3].plot(t,fx/fx[100])

plt.show()
