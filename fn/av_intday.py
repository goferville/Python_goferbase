from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import  time
from datetime import date

def av_inday(tick,intv):
    ts = TimeSeries(key='5O2GGRQDJN5QUIAK', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=tick, interval=intv, outputsize='full')
    fname=tick+'_'+intv+'_'+str(date.today())+'.csv'
    data.to_csv(fname,',')
    print('completed : ', fname)
symbols=['QQQ','DIA','SPY','cron','msft','nvda','amzn', 'amd','gild']
intvls=['1min','5min','60min']
for symb in symbols:
    for intvl in intvls:
        av_inday(symb,intvl)
        time.sleep(20)
