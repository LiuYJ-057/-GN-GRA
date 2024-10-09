# -*- encoding:utf-8 -*- 
import os
from tempfile import tempdir
import numpy as np

listGroup = []
num = 1000
interval = 500
step = 800000
out_step = int(step/interval)
listcount=np.zeros((out_step+1,2),dtype=np.float64)

def myRead(f):
    line = f.readline()
    while line:
        line = line.strip()
        if line == "ITEM: ATOMS id z":
            singleList = []
            line = f.readline()
            line = line.strip()
            while line and not line == "ITEM: TIMESTEP":
                temp = line.split( )
                singleList.append([int(temp[0]),float(temp[1])])
                line = f.readline()
                line = line.strip()
            if singleList:
                singleList = mySort(singleList)
                listGroup.append(singleList)
        line = f.readline()

def mySort(singleList):
    temp = np.array(singleList)
    temp = temp[np.lexsort(temp[:,::-1].T)]
    singleList = temp.tolist()
    return singleList

f = open("funnel_z.txt")
myRead(f)

number=interval
listcount[0][0]=0

for k in range(out_step):
    listcount[k+1][0]=number
    number=number+interval
    
count=0
for i in range(len(listGroup)):
    for j in range(len(listGroup[i])):
        if listGroup[i][j][1]>=0:
            count=count+1
    listcount[i+1][1]=(num-count)
    count=0

if len(listGroup) < out_step:
    for k in range(len(listGroup),out_step):
        listcount[k+1][1]=num


print(listcount)
f.close()
save_path = "funnel_z.csv"  #存储�?csv文件)
np.savetxt(save_path, listcount, delimiter=", ")  #将数组存储在指定地址的文件中

