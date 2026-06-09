class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.min) == 0:
            self.min.append(value)
        else:
            top_min = self.getTop(self.min)
            if value <= top_min:
                self.min.append(value)
        
    def pop(self) -> None:
        top_stack = self.getTop(self.stack)
        top_min = self.getTop(self.min)
        if top_stack == top_min:
            self.min.pop()
        self.stack.pop()

    def top(self) -> int:
        top_stack = self.getTop(self.stack)
        return top_stack

    def getMin(self) -> int:
        top_min = self.getTop(self.min)
        return top_min

    # helper methods
    def getTop(self, stack):
        return stack[len(stack) - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
