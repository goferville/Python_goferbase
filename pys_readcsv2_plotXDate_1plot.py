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
def mouse_move(event):

    if not event.inaxes:
        return
    print('Move')
    x, y = event.xdata, event.ydata
    print(x)
    print(y)
    indx = np.searchsorted(x, [x])[0]  # x is 1-D array since numpy self.x is array of array - Gofer
    x = x[indx]
    #y = y[indx]
    print(x)
    # update the line positions
    lx.set_ydata(float(y))
    ly.set_xdata(x)
df=pd.read_csv("GoogleFinanceTest.csv", parse_dates=['Date'],date_parser=parse_dates)
#construct np array
na1=np.array(df.values)
r = np.rec.fromrecords(na1, names="date,open,high,low,close,volume")
#plot using datetime as x
#Method 1
fig, ax = plt.subplots()
date = r.date.astype('O')
ax.plot(date, r.close, 'o-')
ax.set_title("Default")
fig.autofmt_xdate()
# next we'll write a custom formatter
lx = ax.axhline(y=30,color='k')  # the horiz line
ly = ax.axvline(x=pd.to_datetime('2017/01/01'),color='k')  # the vert line
plt.connect('motion_notify_event', mouse_move)
plt.show()



