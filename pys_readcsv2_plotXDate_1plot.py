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
    mx, my = event.xdata, event.ydata
    #convert mouseX to datetime object
    mx = mdates.num2date(int(mx)).replace(tzinfo=None)
    print(mx)
    print(my)
    #sort datetime object
    indx = np.searchsorted(date, [mx])[0]  #
    x = date[indx]
    y = r.close[indx]
    print(x)
    # update the line positions
    lx.set_ydata(y)
    ly.set_xdata(x)
    txt.set_text('x=%s, y=%3.4f' % (x.strftime('%m/%d/%Y'), y))
    plt.draw()
df=pd.read_csv("GoogleFinanceTest.csv", parse_dates=['Date'],date_parser=parse_dates)
#construct np array
na1=np.array(df.values)
r = np.rec.fromrecords(na1, names="date,open,high,low,close,volume")
#plot using datetime as x

fig, ax = plt.subplots()
date = r.date.astype('O')
ax.plot(date, r.close, 'o-')
ax.set_title("Default")
fig.autofmt_xdate()

lx = ax.axhline(y=30,color='k')  # the horiz line
ly = ax.axvline(x=pd.to_datetime('2017/01/01'),color='k')  # the vert line
plt.connect('motion_notify_event', mouse_move)
txt = ax.text(0.7, 0.9, '', transform=ax.transAxes)
plt.show()



