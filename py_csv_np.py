import csv
import numpy as np

#read csv
reader = csv.reader(open("test.csv", "r"), delimiter=",")
print(reader)
#data to list
x = list(reader)
#first row as attribute names, rest to data array
r = np.rec.fromrecords(x[1:],names=x[0])
print(x)
print("x[1]=",x[1], "x[1][1]=", x[1][1], "x dim=",np.ndim(x),"x[1] dim=", np.ndim(x[1]))
# print(" x shape = ", reader.shape)
#List to Array
npa=np.array(x)
print(npa.shape)
print(npa[1,1])
print("npa", npa)
#sort
ind=np.argsort(npa[:,2])
npa=npa[ind]
print("indexed npa at col 3",npa)
