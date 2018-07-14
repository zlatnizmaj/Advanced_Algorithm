# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 11:29:42 2018
EDX, MIT 6000x
Braching, Iteration

@author: MrGao
"""
x = int(input('Enter an integer: '))
if x%2 == 0:
    print('')
    print('Even')
else:
    print('')
    print('Odd')
print('Done with condititonal!!')

# Nested conditionals
if (x%2 == 0):
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisble by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')