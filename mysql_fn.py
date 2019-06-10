import mysql.connector
from os import listdir
def init(scm):

    # step 1: Connect to a dedicated MySQL server
    '''
    8.0.15, p=3306, x64, standalone server
    '''
    cnx = mysql.connector.connect(user='koala', password='lb555555', host='127.0.0.1')
    print(cnx.is_connected())
    print(cnx.get_server_info())
    # step 2: build a curser
    cur = cnx.cursor(buffered=True)
    sql = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{}'".format(scm)
    # step 3: execute command
    cur.execute(sql)
    print(cur.rowcount)
    # CREATE DATABASE IF NOT EXISTS DBName;
    rows = cur.fetchall()
    # step 4: get results
    # keynote: basic python operation
    # 1 - execute sql : cur.execute(sql)
    # 2 - fetch results : cur.fetchall() or cur.fetchone()
    # 2 - attention: for buffered cursor, cur itself can be use as an iterator
    #     results were in already after querying
    if (rows):
        print('{} exists already'.format(scm), rows)
    else:
        # create database if not exists
        print('{} does not exist'.format(scm), rows)
        cur.execute('CREATE DATABASE {}'.format(scm))

    return cnx, cur
def check_tbs(cnx,cur,db):
    # check all tables
    for tb in table_day_list:
        create_table(cur, db, tb)
    for tb in table_intra_list:
        create_table(cur, db, tb)
    cnx.commit()
def create_table(cur,db,tname):
    sql = "USE {}".format(db)
    cur.execute(sql)
    sql = "SELECT * FROM information_schema.tables WHERE table_name = '{}'".format(tname)
    cur.execute(sql)
    if cur.rowcount:
        print('Table {} exists!'.format(tname))
        return
    sql="CREATE TABLE `{0}`.`{1}` (" \
        "datetime datetime, " \
        "name VARCHAR(10), " \
        "open DECIMAL(12,2), " \
        "high DECIMAL(12,2), " \
        "low DECIMAL(12,2), " \
        "close DECIMAL(12,2), " \
        "volume DECIMAL(12,0)," \
        "PRIMARY KEY(`datetime`, `name`)"\
        ")".format(db,tname)
    print(sql)
    cur.execute(sql)

def load_file2intraday(cnx, cur, db,fname, tname):
    sql="USE {}".format(db)
    cur.execute(sql)
    sql = "SELECT * FROM information_schema.tables WHERE table_name = '{}'".format(tname)
    cur.execute(sql)
    if cur.rowcount:
        print('Table {} exists!'.format(tname))
        #   put date column into a variable var1, then convert it to date format
        # and put back to date column
        # here '%m/%d/%Y' must match in .csv here I have 10/8/2001
        sql="LOAD DATA INFILE '{0}' REPLACE INTO TABLE {1} FIELDS TERMINATED BY ',' LINES " \
            "TERMINATED BY '\r\n' IGNORE 1 LINES (@var1,name,open,high,low,close,volume) " \
            "SET datetime = STR_TO_DATE(@var1,'%Y-%m-%d %H:%i:%S')".format(fname, tname)
        #above datetime format must match in .csv file,
        #here we have 2019-03-25 09:31:00 = %Y-%m-%d %H:%i:%S
        #pay attention to all s[ace, -, /, :   --- all need to match
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
    cnx.commit()
def load_file2day(cnx, cur, db,fname, tname):
    sql="USE {}".format(db)
    cur.execute(sql)
    sql = "SELECT * FROM information_schema.tables WHERE table_name = '{}'".format(tname)
    cur.execute(sql)
    if cur.rowcount:
        print('Table {} exists!'.format(tname))
        #   put date column into a variable var1, then convert it to date format
        # and put back to date column
        # here '%m/%d/%Y' must match in .csv here I have 10/8/2001
        print(fname)#          C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/DIA_day_adj_2019-03-28.csv
        sql="LOAD DATA INFILE '{}' REPLACE INTO TABLE `day` FIELDS TERMINATED BY ',' " \
            "LINES  TERMINATED BY '\r\n' IGNORE 1 LINES (@var1,name,open,high,low,close,adj_close," \
            "volume,@dummy, @dummy) SET date = STR_TO_DATE(@var1,'%Y-%c-%e');".format(fname)
        #above datetime format must match in .csv file,
        #here we have 2019-03-25 09:31:00 = %Y-%m-%d %H:%i:%S
        #pay attention to all s[ace, -, /, :   --- all need to match
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
    cnx.commit()
def tick_listInTable(colName,tableName):
    sql="SELECT DISTINCT {0} FROM {1};".format(colName,tableName)
db='scm1'
table_day_list=['day']
table_intra_list=['1min','5min','15min','60min']
sec_file_path = 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/'
cnx, cur=init(db)

sql="SELECT * FROM information_schema.tables WHERE table_name = '1min'"
cur.execute(sql)
# CREATE DATABASE IF NOT EXISTS DBName;
rows=cur.fetchall()
if(rows):
    print('test_table exists \r\nrows = ', rows,'\r\nrows[0] = ',rows[0],'\r\nrows[0][1] = ', rows[0][1])
else:
    print('test_table does not exist', rows)

fs=listdir(sec_file_path)
for fname in fs:
    if('adj_day' in fname):
        tname='day'
        print("loading {0} to table {1}".format(fname, tname))
        load_file2day(cnx, cur, db, sec_file_path+fname, tname)
    elif('min' in fname):
        for tb in table_intra_list:
            if (tb in fname):
                tname = tb
                print("loading {0} to table {1}".format(fname, tname))
                load_file2intraday(cnx, cur, db, sec_file_path + fname, tname)


'''
fname='QQQ_1min_2019-03-30.csv'
tname='1min'
fname=sec_file_path+fname;
load_file2intraday(cnx, cur, db, fname, tname)
#sec_file_path=r'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/'
fname='DIA_adj_day_2019-03-30.csv'
tname='day'
fname=sec_file_path+fname;
load_file2day(cnx, cur, db, fname, tname
'''
fname='QQQ_1min_2019-03-30.csv'
tname='1min'
fname=sec_file_path+fname;
load_file2intraday(cnx, cur, db, fname, tname)
#sec_file_path=r'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/'
fname='DIA_adj_day_2019-03-30.csv'
tname='day'
fname=sec_file_path+fname;
load_file2day(cnx, cur, db, fname, tname)
