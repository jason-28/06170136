class MinStack:

    def __init__(self):
    
        self.list=[]
        self.len=0
        

    def push(self, x: int) -> None:
        self.list.append(x)
        self.len+=1

    def pop(self) -> None:
        if self.len!=0:
            self.list.pop(self.len-1)
            self.len-=1
        else:
            pass

    def top(self) -> int:
        return self.list[self.len-1]

    def getMin(self) -> int:
        return min(self.list)


