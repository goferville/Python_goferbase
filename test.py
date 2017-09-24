import pandas
import requests
import io
import goferlib.goferGoogleFinance as ggf

stock = 'GOOG'
startdate = 'Jul 08, 2015'
enddate = 'Aug 08, 2017'

rooturl = 'http://www.google.com/finance/historical?q='
query = stock + '&startdate=' + startdate +'&enddate=' + enddate + '&output=csv'

# url = 'http://finance.google.com/finance/historical?q=intc&startdate=Sep+1%2C+2014&enddate=Sep+24%2C+2017&num=30&ei=V23HWYHnMYiljAGawZj4BA&output=csv'
url = 'http://finance.google.com/finance/historical?q=intc&startdate=September+1%2C+2014&enddate=09+24%2C+2017&output=csv'

print(url)
response = requests.get(url)
df = pandas.read_csv(io.StringIO(response.content.decode('utf-8')))

print(df)
# http://finance.google.com/finance/historical?cid=700145&startdate=Sep+1%2C+2014&enddate=Sep+24%2C+2017&num=30&ei=V23HWYHnMYiljAGawZj4BA&output=csv