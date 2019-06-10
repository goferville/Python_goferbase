"""
manipulate data

"""
import mysql.connector
from mysql.connector.errors import Error as dbErr
import  datetime
import time
import pandas as pd

#this this the secured folder to store data files to be loaded
sec_file_path='C:/ProgramData/MySQL/MySQL Server 8.0/Uploads'

# build database connection
database_name='ksql_2018'
try:
    cnx=mysql.connector.connect(user='koala',password='****',host='127.0.0.1', database=database_name)
    print("database: ", database_name, " connection = ", cnx.is_connected())
    print("server version = ", cnx.get_server_info())
    cur = cnx.cursor(buffered=True)
except dbErr as e:
    print(e)
    exit()

# main starts
print("Main")
# create 2 dates - start, stop
d1=(datetime.datetime(2017,2,1))
d2=(datetime.datetime(2017,2,28))
# or using delay to create 2nd date
delDay=7
d2=d1+datetime.timedelta(days=delDay)

#convert to string to be used in sql query
d1s=(datetime.datetime(2017,2,1)).strftime('%Y-%m-%d')
d2s=(datetime.datetime(2017,2,28)).strftime('%Y-%m-%d')

price_limit=36.1
try:
    sql = "select * from table_stk_test where date='2017-02-28'"
    cur.execute(sql)
    for row in cur:
        print(row,'\r\n',row[0],row[1])
    sql = "select * from table_stk_test where " \
          "date>='{0}' and date<='{1}' " \
          "and close<{2}".format(d1s,d2s, (price_limit))
    print(sql)
    cur.execute(sql)
    for row in cur:
        #print specific info with format
        print(row,'\r\n',"date = {:%Y %m %d}".format(row[0]),"open price = ", row[1])

except dbErr as e:
    print(e)
    cnx.rollback()

cnx.close()
