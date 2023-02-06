"""
LIFO - Last In First Out
"""

class maxMinStack():
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) - 1]
    
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()
    
    def push(self , num):
        newMinMax = {"min":num , "max":num}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"] , num)
            newMinMax["max"] = max(lastMinMax["max"] , num)
    
        self.minMaxStack.append(newMinMax)
        self.stack.append(num)

    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]
    
    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]