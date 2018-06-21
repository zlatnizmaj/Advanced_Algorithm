class Node:
    def __init__(self, data, pNext = None):
        self.data = data
        self.pNext = pNext
    
    def getData(self):
        return self.data
    
    def setData(self,value):
        self.data = value
        
    def getpNext(self):
        return self.pNext
    
    def setpNext(self, value):
        self.pNext = value
        
   
            
class LinkedList:
    def __init__(self, head = None):
        self.head = head
        
    def isEmpty(self):
        return self.head == None
    
    def getSize(self):
        return self.size
    
    def AddFirstNode(self,data):
        temp = Node(data)
        if self.head is None:
           self.head = temp
           return
        temp.setpNext(self.head)
        self.head = temp
        
    def insertPost(self,data,index):
        current = self.head
        counter = 0
        Temp = Node(data)

        Prev = None

        if index == 0:
            Temp.setpNext(self.head)
            self.head = Temp
        else:
            while counter < index:
                Prev = current
                current = current.getpNext()
                counter = counter + 1

            Temp.setpNext(Prev.getpNext())
            Prev.setpNext(Temp)
        
        
    def AddLastNode(self,data):
       temp = Node(data)
       if self.head is None:
           self.head = temp
           return
       last = self.head
       while last !=None:
           last = last.getpNext()
       last.next =  temp
       temp.next = None
        
    def Size(self):
        cur = self.head
        count = 0
        while cur != None:
            count = count + 1
            cur = cur.getpNext()
        return count
     
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getpNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getpNext()
    
        if previous == None:
            self.head = current.getpNext()
        else:
            previous.setpNext(current.getpNext())

    def printList(self):
        last = self.head
        while last!=None:
            print(last.getData())
            last = last.getpNext()

mylist = LinkedList()
mylist.AddFirstNode(93)
mylist.AddFirstNode(89)
mylist.AddFirstNode(12)
mylist.AddFirstNode(56)
mylist.AddFirstNode(9)
mylist.insertPost(450,3)
mylist.insertPost(45,3)
mylist.insertPost(11,3)
mylist.insertPost(15,3)
print(mylist.Size())

print(mylist.Size())
print(mylist.search(450))
mylist.printList()







