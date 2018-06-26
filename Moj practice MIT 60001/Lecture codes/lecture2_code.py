# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:25:30 2018
Lecture 2 _code
Branching and Iteration
@author: Administrator
"""

#for i in range(500):
#    print ("hello")

#my_list = [5,2,7,-4,0]
#for i in range (len(my_list)):
#    my_list [i] += 1
#print(my_list)

##############################
# loop until the user enters a positive number:
#num = float(input("Enter a positive number: "))
#while num <= 0.0:
#    num = float(input("Enter a POSITIVE nuber: "))
#    
## loop until the randomly generated number is greater than 0.5
#import random
#num = random.random()
#while num <= 0.5:
#    num = random.random()
#print(num)

#say you want to check whether any value in a list is great than 5
#my_list = [1,2,3,4,5,6,7,8]
#my_list2 = []
#greater_than_five = False
#
#for elem in my_list:
#    if elem >5:
#        greater_than_five = True
#        
#    if (greater_than_five):
#        my_list2.append(elem)
#print (my_list2)    

##################################
## EXAMPLE: perfect squares
##################################
# ans = 0
# neg_flag = False
# x = int(input("Enter an integer: "))
# if x < 0:
#     neg_flag = True
#     x = -x
# while ans**2 < x:
#     ans += 1
# if ans**2 == x:
#     if neg_flag:
#         print(f"Square root of negative {-x} using imaginary number = {ans}i ")
#     else:
#         print("Square root of", x, "is", ans)
# else:
#     if neg_flag:
#         print(-x, "is not a perfect square")
#     else:
#         print(x, "is not a perfect square")

#########################
### Nested Conditional
#########################

# from os import  system
#
# user_x = int(input("Enter number x =  "))
# if user_x % 2 == 0:
#     if user_x % 3 == 0:
#         print("Divisible by 2 and by 3")
#     else:
#         print("Divisible by 2 and not by 3")
# elif user_x % 3 == 0:
#     print("Divisible by 3 and not 2")
# else:
#     print('Divisible not by 2 and not by 3')
#
# system('cls')
# letter_X = str(input('Enter letter need to show: '))
# numXs = int(input('How many times should I print the letter X? '))
# toPrint = ''
# #concatenate X to toPrint numXs times
# i = 0
# while i < numXs:
#     toPrint += letter_X
#     i += 1
# print(toPrint)

#square an interger, the hard way
x = -2
ans = 0
itersLeft = abs(x)
while (itersLeft != 0):
    ans += abs(x)
    itersLeft -= 1
print(str(abs(x)) + '*' + str(abs(x)) + ' = ' + str(ans))

# Executing a break statement terminates the loop
# Find a positive integer that is divisible by both 11 and 12

x = 1
while True:
    if x % 11 == 0 and x % 12 == 0:
        break
    x += 1
print(x, 'is divisible by 11 and 12')