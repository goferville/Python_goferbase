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
def write_newcsv(fname,fdata):
    #write data (list of list) to file with deleleting everything already inside
    #'w'= new write, 'a'= append
    with open(fname, 'w') as fw:
        #with action will close the opened file automatically after loop ends
        csvWriter=csv.writer(fw)
        data=get_data2()
        for row in fdata:
            csvWriter.writerow(row)
        test_row=['al','LD005',33,56,57]
        csvWriter.writerow(test_row)
def read_csv(fname):
    #with different delimiter: reader = csv.reader(f, delimiter="|")
    with open(fname, 'r') as fr:
        csvReader=csv.reader(fr)
        for row in csvReader:
            print(row)
            for e in row:
                print(e)


#==========================================
#main
fname='new_csv.csv'
write_newcsv(fname, get_data2())
read_csv(fname)
