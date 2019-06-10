"""
MYSQL Installation:
install downloaded .msi
-------------------
for mysql module:
install visual studio 2013,or 5,or 7
install python3.7
-------------------

step 1 etc for basic operations
keynote for important applications
-------------------
This program load .csv and put content into a sql table
date was reda and converted to sql date format with a @var1
"""
import mysql.connector
import time
import pandas as pd
def create_table(cur,tname):
    sql = "SELECT * FROM information_schema.tables WHERE table_name = '{}'".format(tname)
    cur.execute(sql)
    if cur.rowcount:
        print('Table {} exists!'.format(tname))
        return
    sql="CREATE TABLE {} (" \
        "date date PRIMARY KEY, " \
        "open DECIMAL(6,2), " \
        "high DECIMAL(6,2), " \
        "low DECIMAL(6,2), " \
        "close DECIMAL(6,2), " \
        "adj_close DECIMAL(10,6), " \
        "volume INT" \
        ")".format(tname)
    print(sql)
    cur.execute(sql)

def load_file2table(cnx, cur, fname, tname):
    sql = "SELECT * FROM information_schema.tables WHERE table_name = '{}'".format(tname)
    cur.execute(sql)
    if cur.rowcount:
        print('Table {} exists!'.format(tname))
        #   put date column into a variable var1, then convert it to date format
        # and put back to date column
        # here '%m/%d/%Y' must match in .csv here I have 10/8/2001
        sql="LOAD DATA INFILE '{0}' REPLACE INTO TABLE {1} FIELDS TERMINATED BY ',' LINES " \
            "TERMINATED BY '\r\n' IGNORE 1 LINES (@var1,open,high,low,close,adj_close,volume) " \
            "SET date = STR_TO_DATE(@var1,'%m/%d/%Y')".format(fname, tname)
        cur.execute(sql)
        print(sql)
        print('file loaded \r\n',cur.description)
    else:
        print('Table {} does not exist!'.format(tname))
    sql = 'select * from {}'.format(tname)
    # cur.execute(sql)
    # sql = "SELECT * FROM test_table"
    cur.execute(sql)
    #results = cur.fetchall()
    print('all loaded records :',cur.rowcount)
    #for row in cur:
    #    print(row)

#this this the secured folder to store data files to be loaded
sec_file_path='C:/ProgramData/MySQL/MySQL Server 8.0/Uploads'
# step 1: Connect to a dedicated MySQL server
'''
8.0.15, p=3306, x64, standalone server
'''
cnx=mysql.connector.connect(user='koala',password='****',host='127.0.0.1', database='ksql_2018')
print(cnx.is_connected())
print(cnx.get_server_info())
# step 2: build a curser
cur = cnx.cursor(buffered=True)
sql="SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ksql_2018'"
# step 3: execute command
cur.execute(sql)
print(cur.rowcount)
# CREATE DATABASE IF NOT EXISTS DBName;
rows=cur.fetchall()
# step 4: get results
# keynote: basic python operation
# 1 - execute sql : cur.execute(sql)
# 2 - fetch results : cur.fetchall() or cur.fetchone()
# 2 - attention: for buffered cursor, cur itself can be use as an iterator
#     results were in already after querying
if(rows):
    print('ksql_2018 exists already', rows)
else:
    #create database if not exists
    print('ksql_2018 does not exist', rows)
    cur.execute('CREATE DATABASE ksql_2018')
sql="SELECT * FROM information_schema.tables WHERE table_name = 'test_table'"
cur.execute(sql)
# CREATE DATABASE IF NOT EXISTS DBName;
rows=cur.fetchall()
if(rows):
    print('test_table exists \r\nrows = ', rows,'\r\nrows[0] = ',rows[0],'\r\nrows[0][1] = ', rows[0][1])
else:
    print('test_table does not exist', rows)
    sql="CREATE TABLE test_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
    cur.execute(sql)
    sql = "INSERT INTO test_table (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    cur.execute(sql, val)
    cnx.commit()
    print(cur.rowcount, "record inserted.")

sql="SELECT * FROM test_table"
cur.execute(sql)
results=cur.fetchall()
print('all records :')
for row in results:
    print(row)
#cur.execute('SELECT DATABASE();')
#cursor.execute('CREATE DATABASE ksql_2018')
#print(cursor.execute('USE ksql_2018'))
#region pandas sql
cur.execute("SELECT STR_TO_DATE( '10/24/2013', '%m/%d/%Y' )")
rows=cur.fetchall()
for row in rows:
    print('date test = ', row )
sql='select * from test_table'
df=pd.read_sql(sql, con=cnx)
print(df.info(),'\r\n', df['name'])

csvfile=sec_file_path+'/sql_testtable_2col.csv'
sql="LOAD DATA INFILE '{0}' IGNORE INTO TABLE {1} FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n' IGNORE 1 " \
    "LINES".format(csvfile, 'test_table')
print(sql)
cur.execute(sql)
print('test file loaded \r\n',cur.description)
#name1='testname1'
#print('format ={}'.format(name1))
#df2.to_sql(name='test_table',con=cnx,if_exists = 'append', index=False, flavor = 'mysql')
#endregion pandas
create_table(cur, 'table_stk_test')
fname=sec_file_path+'/INTC.csv'
load_file2table(cnx, cur,fname,'table_stk_test')

cnx.commit()
cnx.close()

'''

1. Float, double and decimal

https://stackoverflow.com/questions/19601975/storing-statistical-data-do-i-need-decimal-float-or-double

This link does a good job of explaining what you are looking for. Here is what is says:

All these three Types, can be specified by the following Parameters (size, d). Where 
size is the total size of the String, and d represents precision. E.g To store a Number 
like 1234.567, you will set the Datatype to DOUBLE(7, 3) where 7 is the total number of 
digits and 3 is the number of digits to follow the decimal point.

FLOAT and DOUBLE, both represent floating point numbers. A FLOAT is for single-precision, 
while a DOUBLE is for double-precision numbers. A precision from 0 to 23 results in a 4-byte 
single-precision FLOAT column. A precision from 24 to 53 results in an 8-byte double-precision 
DOUBLE column. FLOAT is accurate to approximately 7 decimal places, and DOUBLE upto 14.

Decimal’s declaration and functioning is similar to Double. But there is one big difference 
between floating point values and decimal (numeric) values. We use DECIMAL data type to store 
exact numeric values, where we do not want precision but exact and accurate values. A Decimal 
type can store a Maximum of 65 Digits, with 30 digits after decimal point.

So, for the most accurate and precise value, Decimal would be the best option.


https://code.rohitink.com/2013/06/12/mysql-integer-float-decimal-data-types-differences/

MySQL Integer, Float & Decimal Data Types Differences

MySQL is the Most Popular Database Software when it comes to Websites. All Popular Content 
Management Systems work with MySQL like WordPress, vBulletin, Drupal, etc. But, you are probably 
reading this post because you are designing your own database wish to get a better understanding 
of the Number data types of MySQL, especially their size/capacity.
Integer Types

TINYINT – It Can Hold values from -128 to 127. Or 0 to 255 for Unsigned.

SMALLINT -It can Hold values -32768 to 32767 or 0 to 65535 UNSIGNED. This is most commonly used 
field for most websites.

MEDIUMINT – It can Hold values from -8388608 to 8388607 or 0 to 16777215 UNSIGNED.

INT – It can hold Values from -2147483648 to 2147483647 or 0 to 4294967295 UNSIGNED.

BIGINT – -9223372036854775808 to 9223372036854775807 normal. 0 to 18446744073709551615.

What to store a Bigger Integer? I don’t think MySQL provides anything Larger than BIGINT which 
can store values upto 264, which is a huge Number indeed. To Store Larger Values you can store 
them as Varchar, but won’t be able to process them like Integers.

Do you wish to store only a 4 Digit Number? To do so you can declare the data-type for any field 
as SMALLINT(4). All the above types take a parameter (size), which specifies the No. of Digits to 
be stores. But, you can not do something like TINYINT(8).
Floating Types

There are 3 Such Types in MySQL.

FLOAT
DOUBLE
DECIMAL

All these three Types, can be specified by the following Parameters (size, d). Where size is the 
total size of the String, and d represents precision. E.g To store a Number like 12345.678, 
you will set the Datatype to DOUBLE(8, 3) where 8 is the total no. of digits excluding the 
decimal point, and 3 is the no. of digits to follow the decimal.

FLOAT and DOUBLE, both represent floating point numbers. A FLOAT is for single-precision, 
while a DOUBLE is for double-precision numbers. A precision from 0 to 23 results in a 4-byte 
single-precision FLOAT column. A precision from 24 to 53 results in an 8-byte double-precision 
DOUBLE column. FLOAT is accurate to approximately 7 decimal places, and DOUBLE upto 14.

Decimal’s declaration and functioning is similar to Double. But there is one big difference 
between floating point values and decimal (numeric) values. We use DECIMAL data type to store 
exact numeric values, where we do not want precision but exact and accurate values. A Decimal t
ype can store a Maximum of 65 Digits, with 30 digits after decimal point.

For those who did not understand, let me explain with an Example. Create 2 Columns with Types 
Double and Decimal and Store value 1.95 in both of them. If you print each column as Integer 
then you will see than Double Column has printed 1, while Decimal column printed 2.

Generally, Float values are good for scientific Calculations, but should not be used for 
Financial/Monetary Values. For Business Oriented Math, always use Decimal.

'''
