# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 08:47:27 2018

@author: Administrator
"""

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

# doi co so 10 sang co so 2
def convert2B(val):
    st = Stack()
    while (val > 0):
#        print (val % 2)
        st.push(str(val % 2))
        val = val // 2
    popStr = ""    
    while (st.isEmpty()== True):
        popStr = popStr + str(st.pop())
    print (popStr)     
   

n = int(input("Input a number:= "))
convert2B(n)

#s = Stack()
#print(s.isEmpty())
#s.push(4)
#s.push(5)
#print(s.peek())
#s.push(6)
#print(s.size())
#print(s.isEmpty())
#s.push(8.4)
