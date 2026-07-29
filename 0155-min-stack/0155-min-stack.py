class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append((value,value))
        else:
            minVal=self.getMin()
            self.stack.append((value,min(value,minVal)))

        

    def pop(self) -> None:
        if not self.stack:
            return -1
        else:
            self.stack.pop()
        

    def top(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()