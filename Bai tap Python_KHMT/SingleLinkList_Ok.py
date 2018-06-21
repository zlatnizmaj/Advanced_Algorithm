# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class SLLList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head == None
    
    def addLast(self, val):
        node = Node(val)
        if (self.isEmpty() == False):
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
    def addFirst(self, val):
        node = Node(val)
        if (self.isEmpty() == False):
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
    
    def size(self):
        current_node = self.head
        counter = 0
        while (current_node is not None):
            counter=counter+1
            current_node = current_node.next
        return counter

    def print_List(self):
        tmp = self.head
        while tmp != None:
            print(tmp.val)
            tmp = tmp.next

            
#Main function
if __name__ == "__main__":
    SLL = SLLList()
    SLL.addFirst(20)
    SLL.addFirst(13)
    SLL.addFirst(24)
    SLL.print_List()
    SLL.addLast(56)
    SLL.print_List()
    print (SLL.size())
   
    