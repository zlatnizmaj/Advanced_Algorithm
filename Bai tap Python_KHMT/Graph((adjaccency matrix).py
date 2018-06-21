# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 09:57:01 2018

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
        self.check =[True]*vertices
        
    def DFS(self, i):
        self.visited[i] = True
        self.a.append(i)
        for j in range(self.v):
            if (self.graph[i][j]>0) and self.visited[j]==False:
                self.DFS(j)
    
    def Connectivity(self):
        self.DFS(0)
        for i in range(self.v):
            if self.check[i]: return False
        return True
    
    def CountConnectivity(self):
        count = 1
        self.DFS(0)
        for k in range(self.v):
            if self.check[k]:
                count += 1
                self.DFS(k)
        return count
    
    def Dijstra2Node(self, Fnode, Lnode):
        vocung = 100000
        for i in range(self.v):
            for j in range(self.v):
                if ((i != j) and self.graph[i][j] == 0):
                    self.graph[i][j] = vocung
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
            for j in range(self.v):
                if (S[j] == False and L[i] + self.graph[i][j] < L[j]):
                    L[j] = L[i] + self.graph[i][j]
                    P[j] = i
        print(L[Lnode])  
        if (L[Lnode] > 0 and L[Lnode] < vocung):
            print("Length of ", Fnode+1, " to ", Lnode+1, "is: ", L[Lnode])
            while (i != Fnode):
                print(i, "<----")
                i = P[i]
            print(Fnode+1)
        else:
            print("No path from %d to %d ", Fnode, Lnode)
g = Graph(6)
g.graph = [[0 , 7 , 9 , 0 , 0, 14],
           [7 , 0 , 10, 15, 0, 0 ], 
           [9 , 10, 0 , 11, 0, 2 ],
           [0 , 15, 11, 0 , 6, 0 ],
           [0 , 0 , 0 , 6 , 0, 9 ],
           [14, 0 , 2 , 0 , 9, 0 ]]

print("Duong di ngan nhat: ")
g.Dijstra2Node(0,4)
g.Dijstra2Node(0,5)
g.Dijstra2Node(0,3)


#for i in range(g.v):
#    g.visited = [False]*g.v
#    g.a=[]
#    g.DFS(i)
#    print(g.a)
#g.DFS(1) #
#g.DFS(1)
#print(g.a)