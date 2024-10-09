import sys
import os
import numpy as np
import glob
import pandas as pd
from csv import reader
import csv as csv

with open(r'/data/wenzh/liuyanjun/lammps_graph/1/exchange_miu/miu=0.01/funnel_z.csv', 'r', encoding='utf-8') as f:  # 打开文件
    csv_reader = reader(f)
    # Passing the cav_reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    last_line=[0,0]
    last_line[0] = float(list_of_rows[-1][0])
    last_line[1] = float(list_of_rows[-1][1])
    print(last_line)

with open(r'/data/wenzh/liuyanjun/lammps_graph/1/exchange_miu/miu=0.01/result.csv', 'a',newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(last_line)