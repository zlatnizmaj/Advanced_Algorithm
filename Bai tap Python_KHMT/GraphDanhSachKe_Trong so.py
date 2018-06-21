# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 10:53:55 2018

@author: Administrator
"""
# do thi co trong so
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.v = vertices
        self.visited = [False]*(vertices)
    
    def addEdge(self, src, dest, weight):
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)
        #Undirection graph so weight(u,v) = weight(v,u)
        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)

    def Dijstra2Node(self, Fnode, Lnode):
        vocung = 100000
#        for i in range(self.v):
#            for j in range(self.v):
#                if ((i != j) and self.graph[i][j] == 0):
#                    self.graph[i][j] = vocung
        S = [False]*(self.v)
        P = []
        L = []
        for k in range(self.v):
            P.append(Fnode)
            L.append(vocung)
        L[Fnode] = 0
        
        while (S[Lnode] == False):
            for i in range(self.v):
                if ((S[i] == False) and L[i] < vocung):
                    break
            if (i >= self.v):
                break
            for j in range(self.v):
                if ((S[j] == False) and L[i] > L[j]):
                    i = j
            S[i] = True
            
            for k in range(len(self.graph[i])):
                j = (self.graph[i][k])[0]
                cost = (self.graph[i][k])[1]
                if (S[j] == False and L[i] + cost < L[j]):
                    L[j] = L[i] + cost
                    P[j] = i
                    
        print(L[Lnode])  
        if (L[Lnode] > 0 and L[Lnode] < vocung):
            print("Length of ", Fnode, " to ", Lnode, "is: ", L[Lnode])
            while (i != Fnode):
                print(i, "<----")
                i = P[i]
            print(Fnode)
        else:
            print("No path from %d to %d ", Fnode, Lnode)
                          
g = Graph(4)
g.addEdge(0, 1, 1)
g.addEdge(1, 2, 2)
g.addEdge(2, 3, 3)
g.addEdge(0, 3, 9)
#g.addEdge(2, 3, 7)
#g.addEdge(2, 5, 4)
g.Dijstra2Node(0,3)
#for i in range(3):
##    print(g.graph[i])
#    print("[ ", i, " = ",g.graph[i])
#    
#print(g.graph[0][1])

print("Dinh ke voi 0",(g.graph[0][1])[0])
print("Trong so cua dinh ke voi dinh 0", (g.graph[0][1])[1])
