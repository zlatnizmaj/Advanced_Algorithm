# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 11:15:22 2018

@author: Administrator
"""

import sys
print('Python: {}'.format(sys.version))

import scipy
print('scipy: {}'.format(scipy.__version__))

import numpy
print('numpy: {}'.format(numpy.__version__))

import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))

import pandas
print('pandas: {}'.format(pandas.__version__))

from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

names = ['D-C', 'R_C', 'D-D', 'R-D', 'Loai hoa']
dataset = pandas.read_csv('Iris.txt', names=names)
print(dataset.shape)

print(dataset.head(20))
print(dataset.describe())
print(dataset.groupby('Loai hoa').size())
dataset.plot(kind='box', subplots = True, layout=(2,2), sharex=False,sharey=False)
dataset.hist()
scatter_matrix(dataset)

plt.show()
