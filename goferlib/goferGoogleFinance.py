import pandas as pd
import io
import requests
import time
import datetime as dt

def parse_dates(x):
    return (pd.to_datetime(x))



def getGoogHistDayData(symbol, startdate, enddate):
    """

    :param symbol: String
    :param startdate: datetime
    :param enddate: datetime
    :param csvName: *.csv
    :return: pandas dataframe
    symbol='AAPL'
    startdate=datetime.datetime(2015,3,12)
    """
    """
    return pandas dataframe with columns:Date	Open	High	Low	Close	Volume
    Google has all adjusted price
    """
    sD=startdate.strftime("%d")
    sM=startdate.strftime("%B")
    sY=startdate.strftime("%Y")
    eD = enddate.strftime("%d")
    eM = enddate.strftime("%B")
    eY = enddate.strftime("%Y")
    stock_url = 'http://finance.google.com/finance/historical?q='+symbol+'&startdate='+sM+'+'+sD+'%2C+'+sY+'&enddate='+eM+'+'+eD+'%2C+'+eY+'&output=csv'

    print(stock_url)

    response = requests.get(stock_url)
    stock_data = pd.read_csv(io.StringIO(response.content.decode('utf-8')), parse_dates=['Date'], date_parser=parse_dates)
    return stock_data
def getGoogHistDayData2Csv(symbol, startdate, enddate,csvName):
    """

    :param symbol: String
    :param startdate: datetime
    :param enddate: datetime
    :param csvName: *.csv
    :return: saved csv file
    """
    histData=getGoogHistDayData(symbol, startdate, enddate)
    histData.to_csv(csvName, index=False, encoding='utf-8')
