import pandas as pd
import io
import requests
import time
import datetime as dt
import goferlib.goferGoogleFinance as ggf

if __name__ == '__main__':
    startDate=dt.datetime(2015,3,12)
    endDate=dt.datetime.now()
    #apple_data = getGoogHistDayData('AAPL',startDate,endDate)
    ggf.getGoogHistDayData2Csv('INTC', startDate, endDate, 'testIntc2.csv')
    #ggf.getGoogHistDayData("aapl",startDate,endDate)


"""
Notes on Data Structure

Unlike the Yahoo! Finance API, this will not return the adjusted close 
as a separate column. In Automated Trading with R, we go to great lengths 
to use the adjusted close to obtain adjusted open, adjusted high, 
and adjusted low. The Google Finance API used here returns all of that 
information for you. So, there is no column named “adjusted close”. 
All of the data is adjusted in advance.

Advanced users may be disappointed by this, because there is some 
interesting information regarding splits and dividends to be gained 
from the disparity between raw and adjusted closing prices. Regardless, 
most users should be able to use the data returned by this API to accomplish 
their simulation goals.
"""
