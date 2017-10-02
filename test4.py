import csv
from urllib import request

url = 'http://winterolympicsmedals.com/medals.csv'
cr = request.urlopen(url).read()
cr2=str(cr,'utf-8')
print(cr2)
with open('file1.csv', 'wb') as fx: # bytes, hence mode 'wb'
    fx.write(cr)
