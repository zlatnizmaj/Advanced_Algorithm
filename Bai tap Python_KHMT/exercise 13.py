# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 11:06:56 2018

@author: Administrator
"""

import glob
path = 'D:\\@JUGNAM#\\06 Advanced Algorithm\\01 Bai tap Python\\*.txt'

files= glob.glob(path)

for file in files:
    f=open(file, 'r')
    print('%s' % f.readlines())
    f.close()