"""
Installation:
install downloaded .msi
for mysql module:
install visual studio 2013,or 5,or 7
install python3.7
-------------------

step 1 etc for basic operations
keynote for important applications
"""
import mysql.connector
import time
import pandas as pd
sec_file_path='C:/ProgramData/MySQL/MySQL Server 8.0/Uploads'
# step 1: Connect to a dedicated MySQL server
cnx=mysql.connector.connect(user='koala',password='lb555555',host='127.0.0.1', database='ksql_2018')
print(cnx.is_connected())
print(cnx.get_server_info())
# step 2: build a curser
cur = cnx.cursor()
sql="SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ksql_2018'"
# step 3: execute command
cur.execute(sql)
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
sql='select * from test_table'
df=pd.read_sql(sql, con=cnx)
print(df.info(),'\r\n', df['name'])
df2 = pd.DataFrame({'name' : ['true', 'false', 'true', 'false',
                           'true', 'false', 'true', 'false'],
                    'address' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three']
                    })
df2 = pd.DataFrame({'name' : ['Mary'],
                    'address' : ['one']
                    })
print(df2)
csvfile=sec_file_path+'/sql_testtable_2col.csv'
sql="LOAD DATA INFILE '{}' IGNORE INTO TABLE test_table FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n' IGNORE 1 " \
    "LINES".format(csvfile)
print(sql)
cur.execute(sql)
#name1='testname1'
#print('format ={}'.format(name1))
#df2.to_sql(name='test_table',con=cnx,if_exists = 'append', index=False, flavor = 'mysql')
#endregion pandas
cnx.commit()
cnx.close()
