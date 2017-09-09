class setofstacks():
    def __init__(self,capacity):
        self.stacks = [[]]
        self.capacity = capacity
    def push(self,elem):
        stack = self.stacks[-1]
        if len(stack) < self.capacity:
            stack.append(elem)
        else:
            newstack = [elem]
            self.stacks.append(newstack)
    def pop(self):
        stack = self.stacks[-1]
        elem = stack[-1]
        stack = stack[:-1]
        self.stacks[-1] = stack
        if not stack:
            self.stacks = self.stacks[:-1]
        return elem
x = setofstacks(2)
print(x.push(1))
print(x.push(2))
x.push(3)
print(x.pop())
print(x.pop())
print(x.pop())
