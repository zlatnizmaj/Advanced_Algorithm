# -*- coding: utf-8 -*-
"""
Created on Fri May 18 08:37:48 2018

@author: Administrator
"""

class Graph():
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        self.visited = [] #khai bao visited la list
        for i in range(vertices):
            self.visited.append(False)
#        self.visited = [False]*vertices
        self.a = []
        
    def DFS(self, i):
        self.visited[i] = True
        self.a.append(i)
        for j in range(self.v):
            if (self.graph[i][j]>0) and self.visited[j]==False:
                self.DFS(j)

g = Graph(6)
g.graph = [[0, 1, 1, 0, 0, 0],
           [1, 0, 0, 0, 0, 0], 
           [1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0],
           [0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0]]
for i in range(g.v):
    g.visited = [False]*g.v
    g.a=[]
    g.DFS(i)
    print(g.a)