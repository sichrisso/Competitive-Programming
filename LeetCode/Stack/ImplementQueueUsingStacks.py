class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        if len(self.s2) != 0:
            while(len(self.s2) !=0):
                rem = self.s2.pop()
                self.s1.append(rem)
            self.s1.append(x)
        else:
            self.s1.append(x)

    def pop(self) -> int:
        while(len(self.s1) !=0):
            rem = self.s1.pop()
            self.s2.append(rem)
        return self.s2.pop()

    def peek(self) -> int:
        if len(self.s1) == 0:
            return self.s2[-1]
        else:
            return self.s1[0]
        

    def empty(self) -> bool:
        if len(self.s1) == 0 and len(self.s2) == 0:
            return True
        else:
            return False
        
