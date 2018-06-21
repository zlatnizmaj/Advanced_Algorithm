# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 11:11:34 2018

@author: Administrator
"""

from os import listdir
from os.path import isfile, join
mypath= "D:\\@JUGNAM#\\06 Advanced Algorithm\\01 Bai tap Python\\"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)