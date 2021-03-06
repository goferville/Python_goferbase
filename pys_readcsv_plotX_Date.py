import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from datetime import datetime
import pandas as pd
# use pandas to read csv so can get datetime object in pd data frame
def parse_dates(x):
    return (pd.to_datetime(x))

df=pd.read_csv("AMD.csv", parse_dates=['Date'],date_parser=parse_dates)
#construct np array
na1=np.array(df.values)
r = np.rec.fromrecords(na1, names="date,open,high,low,close,volume")
#plot using datetime as x
#Method 1
fig, ax = plt.subplots(ncols=2, sharex=False, figsize=(8, 4))
date = r.date.astype('O')
ax[0].plot(date, r.close, 'o-')
ax[0].set_title("Default")
fig.autofmt_xdate()
# next we'll write a custom formatter
N = len(r)
ind = np.arange(N)  # the evenly spaced plot indices


def format_date(x, pos=None):
    thisind = np.clip(int(x+0.5 ), 0, N - 1)
    return date[thisind].strftime('%Y-%m-%d')


ax[1].plot(ind, r.close, 'o-')
ax[1].xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
ax[1].set_title("Custom tick formatter")
fig.autofmt_xdate()
#plt.subplots_adjust(hspace = 1)
plt.show()
