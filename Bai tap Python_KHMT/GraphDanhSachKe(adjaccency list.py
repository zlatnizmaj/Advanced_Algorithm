# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 10:39:13 2018

@author: Jugnam
"""
from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.v = vertices
        self.visited = [False]*(vertices)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def DFS(self, i):
        self.visited[i] = True
        print(i)
        for j in self.graph[i]:
            if self.visited[j] == False:
                self.DFS(j)
                
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

for i in range(4):
#    print(g.graph[i])
    print("[ ", i, "= ",g.graph[i])

print("Following is DFS")
g.DFS(0)

