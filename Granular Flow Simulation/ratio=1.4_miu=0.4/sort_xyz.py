import os
from tempfile import tempdir
import numpy as np

listGroup = []
num = 1000
interval = 500
step = 700000
out_step = int(step/interval)
listcount=np.zeros((out_step+1,4),dtype=np.float64)

def myRead(f):
    line = f.readline()
    while line:
        line = line.strip()
        if line == "ITEM: ATOMS id x y z radius":
            singleList = []
            line = f.readline()
            line = line.strip()
            while line and not line == "ITEM: TIMESTEP":
                temp = line.split( )
                singleList.append([int(temp[0]),float(temp[1]),float(temp[2]),float(temp[3]),float(temp[4])])
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

f = open("funnel_xyz.txt")
myRead(f)
f.close() 

print(type(listGroup))
f = open("test.txt",'w')
for i in range(len(listGroup)):
    f.write("1000\n")
    for j in range(len(listGroup[i])):
        singleline = format(str(listGroup[i][j][1])+' '+str(listGroup[i][j][2])+' '+str(listGroup[i][j][3])+' '+str(listGroup[i][j][4])+"\n")
        f.write(singleline)
f.close()


