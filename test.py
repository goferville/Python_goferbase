
"""
GogleFinanceTest.csv
"""
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import pandas as pd
import numpy as np
import datetime as dt
from matplotlib.dates import date2num
from matplotlib.dates import DateFormatter, WeekdayLocator,\
    DayLocator, MONDAY

x = np.array([(1.0, 2), (3.0, 4)], dtype=[('x', float), ('y', int)])
#print(x)
x = x.view(np.recarray)
print(x.x[1])
print(x.dtype)
#np.recarray((2,),dtype=[('x', int), ('y', float), ('z', int)])
#y=np.recarray([(1.0, 2), (3.0, 4)], dtype=[('x', '<f8'), ('y', '<i4')])