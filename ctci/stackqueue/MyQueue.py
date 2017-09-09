class MyQueue():
    def __init__(self):
        self.first = []
        self.second = []
    def enqueue(self,elem):
        self.first.append(elem)
    def dequeue(self):
        self.second = self.first[::-1]
        elem = self.second.pop()
        self.first = self.second[::-1]
        self.second = []
        return elem

x = MyQueue()
x.enqueue(1)
x.enqueue(2)
x.enqueue(3)
print(x.dequeue())
print(x.dequeue())
print(x.dequeue())
