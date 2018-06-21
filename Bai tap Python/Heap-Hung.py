def makeHeap(a, i):
    #Check co ton tai 2*i+1, 2*i+2 khong?
    posMax=i
    if (2*i+1<=n and 2*i+2>n): posMax =2*i+1        
    if (2*i+2<=n):
        if (a[2*i+1] > a[2*i+2]):
            posMax = 2*i+1
        else:
            posMax = 2*i+2   
            
       
    if (a[i]< a[posMax]):
        tmp= a[i]
        a[i]= a[posMax]
        a[posMax]=tmp
        makeHeap(a,posMax)  
    
def makeheapMax(a, i): 
    left = 2*i+1
    right = 2*i+2
    posMax = i      
    if (left <= n and a[left] > a[i]):
        posMax=left
    else:
        posMax=i
     
    if(right <= n and a[right] > a[posMax]):
        posMax=right
    if (posMax != i):
        tmp = a[i]
        a[i]= a[posMax]
        a[posMax] = tmp         
        makeheapMax(a, posMax)
 
def buildHeap(a):
    for i in range(len(a)//2-1,-1,-1): makeHeap(a,i)
        
 
 
 
a= [1, 2, 7, 5, 4, 9, 12, 15]
n=len(a)-1
    
print(" ".join([str(a[i]) for i in range(0,n+1)]))
buildHeap(a)
print(" ".join([str(a[i]) for i in range(0,n+1)]))