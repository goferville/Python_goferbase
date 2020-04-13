import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib.dates import (MONDAY, DateFormatter, MonthLocator,
                              WeekdayLocator, HourLocator,  date2num)
import os.path
import io

from mplfinance.original_flavor import candlestick_ohlc
infile='spy_day.csv'
houFmt=DateFormatter('%d/%Y%m%d %H')
minFmt=DateFormatter('%Y/%m/%d %H:%M')
allHours=HourLocator()
#width=0.5 #for day
width=0.5/60/24 #for minute
quotes = pd.read_csv(infile,
                     index_col=0,
                     parse_dates=True,
                     infer_datetime_format=True)
fig, ax = plt.subplots()
ax.xaxis.set_major_locator(allHours)
ax.xaxis.set_major_formatter(houFmt)
candlestick_ohlc(ax, zip(date2num(quotes.index.to_pydatetime()),
                         quotes['open'], quotes['high'],
                         quotes['low'], quotes['close']),
                 width=width, colorup='#008800',colordown='r', alpha=0.8)

#ax.plot(quotes['high'],style='scatter')
ax.scatter(x=date2num(quotes.index.to_pydatetime()),y=quotes['high'], s=30, marker='>', color='#00ff00')
ax.scatter(x=date2num(quotes.index.to_pydatetime()),y=quotes['low'], s=30, marker='<', color='purple')
#quotes['high'].plot.scatter(ax)
#ax.scatter(zip(date2num(quotes.index.to_pydatetime())),zip(quotes['low'][:1]))
# Setting labels & titles
ax.set_xlabel('Date')
ax.set_ylabel('Price')
fig.suptitle('InDay SPY')

ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
print(quotes['low'])
plt.show()
