# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:25:20 2018
Bài toán Đệ quy
Fibonacci:
    N=0, F=0
    N=1, F=1
    F(n) = F(n-1) + F(n-2)
    GCD(a,b)
    a= b
    a>b GCD(a-b, b)
        GCD(a, b-a)
Khử đệ quy
    1. Vòng lặp
    2. Hàm đệ quy ARSAC-Stack
@author: Administrator
"""

def FibonacciRecursion(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return FibonacciRecursion(n-1) + FibonacciRecursion(n-2)

def GCD(a, b):
    if (a==b):
        return a
    elif (a>b):
        return GCD(a-b, b)
    else:
        return GCD(a, b-a)

def GCDNoRecursion(a, b):
    while (a!=b):
        if (a>b):
            a= a-b
        else:
            b= b-a
    return a
#print (FibonacciRecursion(5))
#print (GCD(4,10))
#print (GCDNoRecursion(4,10))
# sử dụng STACK
class Stack:
    def __init__(self):
        self.items = [] # khai bao List
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
#def GCDStack(a, b): 
#    s1 = Stack()
#    s2 = Stack()
#    s1.push(a)
#    s2.push(b)
#    print (s1.peek())
#    print (s2.peek())
#    while (s1.peek()!= s2.peek()):
#        if (s1.peek()> s2.peek()):
#           s1.push(s1.pop()-s2.peek())
#        else:
#           s2.push(s2.pop()-s1.peek())
#    return s1.pop()
#print (GCDStack(4,10))

#def HanoiTower(n, A, B, C):
#    if(n==1):
#        print ("Di chuyen 1 dia tu", A, " sang ", C)
#    else:
#        HanoiTower(n-1, A, C, B)
#        print ("Di chuyen 1 dia tu", A, " sang ", C)
#        HanoiTower(n-1, B, A, C)
#
#print (HanoiTower(4, "A", "B", "C"))
"""
(4,A,B,C) (3,A,C,B) (2,A,B,C)
  (A,C)   (3,B,A,C)
   (A,B)    (2,C,A,B)
(A,B) (A,C) (B,C) (A,B)

Quy hoach dong Bottom-up
L(1) = 1
L(j) = max(L(i)+1, 1)
j:0->i
a[j] > a[i]
"""    
def lis(arr):
    n = len(arr)
    lis = [1]*n # lis =[] in range(n) lis.append(1)
    for i in range (1,n):
        for j in range (0,i):
            if arr[i]>arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j]+1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])
        print (maximum, " ", lis[i])
    tmp = maximum
    for i in range(n-1, -1, -1):
        if (tmp == lis[i]):
            print(arr[i])
            tmp -=1
    return maximum


arr =[10,22,9,33,21,50,41,20] # 1, 2, 1, 
print("Lenght of lis is", lis(arr))
# Cho day a1, a2, ..an. Tim 1 day con cua day do co tong bang S
# 1,4,7,5,8,9,2 S=20
# Bài toán balô, giá trị và khối lượng đựng của balô