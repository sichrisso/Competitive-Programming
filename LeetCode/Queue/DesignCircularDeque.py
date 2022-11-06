class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None]*k
        self.front = 0
        self.rear = 0
        self.size = 0
       
    def insertFront(self, value: int) -> bool:
        if self.isFull(): 
            return False
        elif self.queue[self.front] == None:
            self.queue[self.front] = value
            self.rear = (self.rear + 1) % self.k
            self.size += 1
            return True
        elif self.queue[self.front] != None:
            self.front = (self.front - 1) % self.k
            self.queue[self.front] = value
            self.size += 1
            return True
 
    def insertLast(self, value: int) -> bool:
        if self.isFull(): 
            return False
        else:
            self.queue[self.rear] = value
            self.size += 1
            self.rear = (self.rear + 1) % self.k
            return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty(): 
            return False
        else:
            self.queue[self.front] = None
            self.size -= 1
            self.front = (self.front + 1) % self.k
            return True
        
        

    def deleteLast(self) -> bool:
        if self.isEmpty(): 
            return False
        else:
            self.queue[self.rear - 1] = None
            self.size -= 1
            self.rear = (self.rear - 1) % self.k
            return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear - 1]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.k
        