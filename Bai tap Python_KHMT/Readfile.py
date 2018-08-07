# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 11:06:51 2018

@author: UNUC
"""
"""
import glob
path = 'E:\\test.txt'
files = glob.glob(path)
for file in files:
    f = open(file, 'r')
    print('%s' %f.readlines())
    f.close()
    
from os import listdir
from os.path import isfile, join
mypath = "E:\\"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]
print(onlyfiles)
"""
import sys
print('Python:{}'.format(sys.version))
import scipy
print('scipy:{}'.format(scipy.__version__))

import pandas
print('pandas: {}'.format(pandas.__version__))
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

names = ['D-C','R-C','D-D','R-D','Loai hoa']
dataset = pandas.read_csv('Iris.txt',names = names)
print(dataset.shape)
print(dataset.head(20))
print(dataset.describe())
print(dataset.groupby('Loai hoa').size())
dataset.plot(kind = 'box', subplots = True, layout = (2,2), sharex = False, sharey = False)
dataset.hist()
scatter_matrix(dataset)

plt.show()
