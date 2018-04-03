import csv, numpy

def get_data1():
    data = [['SN', 'Person', 'DOB'],
              ['1', 'John', '18/1/1997'],
              ['2', 'Marie', '19/2/1998'],
              ['3', 'Simon', '20/3/1999'],
              ['4', 'Erik', '21/4/2000'],
              ['5', 'Ana', '22/5/2001']]
    return data
def get_data2():
    data = [['name', 'sn', 'depth','height'],
              ['bl', 'LD001', 32, 24],
              ['jl', 'LD003', 33, 55]]
    return data
def wr_newcsv(fname,fdata):
    #write data (list of list) to file with deleleting everything already inside
    with open(fname, 'w') as fw:
        #with action will close the opened file automatically after loop ends
        csvWriter=csv.writer(fw)
        data=get_data2()
        for row in fdata:
            csvWriter.writerow(row)


#==========================================
#main

wr_newcsv('new_csv.csv', get_data2())
