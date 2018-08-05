class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = [] # indice of the minimum in self.stack
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        
        # keep track of the indice of the minimum
        # from self.stack
        size = len(self.stack)
        if size == 1:
            self.min.append(0)
        else:
            self.min.append(size-1 if x < self.stack[self.min[-1]] else self.min[-1])
        

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            del self.min[-1]
            del self.stack[-1]
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[self.min[-1]]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()