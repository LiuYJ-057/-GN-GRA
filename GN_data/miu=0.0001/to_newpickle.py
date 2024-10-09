from os.path import dirname, join as pjoin
import math
import csv
import os
import numpy as np
import pickle

ATOM_NUMBER = 1000
L = 100
# 训练集个数
N = 1000
listGroup = []
aGroup = []
num = 1000
interval = 500
step = 800000
out_step = int(step/interval)
listcount=np.zeros((out_step+1,2),dtype=np.float64)

def myRead(f):
    line = f.readline()
    while line:
        line = line.strip()
        if line == "ITEM: ATOMS id y z":
            singleList = []
            aList = []
            line = f.readline()
            line = line.strip()
            while line and not line == "ITEM: TIMESTEP":
                temp = line.split( )
                singleList.append([int(temp[0]),float(temp[1]),float(temp[2])])
                aList.append([float(temp[1]),float(temp[2])])
                line = f.readline()
                line = line.strip()
            if singleList:
                singleList = mySort(singleList)
                listGroup.append(singleList)

            if aList:
                aList = mySort(aList)
                aGroup.append(aList)
        line = f.readline()

def mySort(singleList):
    temp = np.array(singleList)
    temp = temp[np.lexsort(temp[:,::-1].T)]
    singleList = temp.tolist()
    return singleList

f = open("funnel_yz_43400.txt")
myRead(f)
rr=[50,100]
for i in range(len(aGroup)):
    if len(aGroup[i])<1000:
        for j in range(0,1000-len(aGroup[i])):
            aGroup[i].append(rr)

# 初始位置
positions = np.array(aGroup[0])

# 其他位置
target_positions = []
for i in range (1,len(aGroup)):
    target_positions.append(np.array(aGroup[i]))
# time
time = []
# 初始粒子种类
atom_type=[]
for i in range (0,1000):
    atom_type.append(1)
atom_type=np.array(atom_type)

# box
box = np.array([L, L])
# φ
fai = []
# metadata
metadata = {'L': L, 'N': N}

number = interval
listcount[0][0] = 0

for k in range(out_step):
    listcount[k + 1][0] = number
    time.append(number)
    number = number + interval

count = 0
for i in range(len(listGroup)):
    for j in range(len(listGroup[i])):
        if listGroup[i][j][2] >= 40:
             count = count + 1
    listcount[i + 1][1] = (num - count)
    fai.append(float(listcount[i + 1][1]))
    count = 0
fai[0]=0.0
fai[1] = 0.0
fai[2] = 0.0
fai[3] = 0.0
fai[4] = 0.0
fai=np.array(fai)

if len(listGroup) < out_step:
    for k in range(len(listGroup), out_step):
        listcount[k + 1][1] = num

train_path = './pickletrain_miu=0.0001/'  # 噪声视野角改
if not os.path.isdir(train_path):
    os.makedirs(train_path)
path = pjoin(train_path + 'test49.pickle')
fa = open(path, 'wb')

datapickle = {'positions': positions, 'types': atom_type, 'box': box, 'time': time, 'targets': fai,
                'metadata': metadata,
                'trajectory_target_positions': target_positions, }
pickle.dump(datapickle, fa)
fa.close()

