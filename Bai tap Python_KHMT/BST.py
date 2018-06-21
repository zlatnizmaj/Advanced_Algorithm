# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:21:16 2018

@author: Administrator
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def isEmpty(self):
        return self.root == None
    def add(self, val):
        p = Node(val)
        tmp=self.root
        pre = None
        while (tmp is not None):
            pre = tmp
            if(val<=tmp.val):
                tmp=tmp.left
            else:
                tmp=tmp.right
        if (self.root is None):
            self.root = p
        else:
            if (val > pre.val):
                pre.right = p
            else:
                pre.left = p
    def preorder(self, t):
        if(t is not None):
            print(" ", t.val)
            self.preorder(t.left)
            self.preorder(t.right)
    def postorder(self, t):
        if(t is not None):
            print(" ", t.val)
            self.postorder(t.left)
            self.postorder(t.right)
    # tinh chieu cao cua Cay
    def CalHeight(self, p):
        if(p is None):
            return 0
        a=self.CalHeight(p.left)
        b=self.CalHeight(p.right)
        if(a>b):
            return a+1
        else:
            return b+1

a=[4,5,7,9,1,2]
bst=BST()
for i in range(len(a)):
    bst.add(a[i])
    
bst.preorder(bst.root)
print("Chieu cao cua cay BST: ",bst.CalHeight(bst.root))
#bst.postorder(bst.root)