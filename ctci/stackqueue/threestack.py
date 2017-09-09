class threestack():
    def __init__(self,numstacks):
        self.numstacks = numstacks
        self.stackarr = []
    def push(self,elem,numstack):
        self.stackarr.append((elem,numstack))
    def peek(self,numstack):
        for i in range(-1,-len(self.stackarr)-1,-1):
            elem, stacknum = self.stackarr[i][0], self.stackarr[i][1]
            if stacknum == numstack:
                return elem
        raise ValueError
    def pop(self,numstack):
        for i in range(-1,-len(self.stackarr)-1,-1):
            elem, stacknum = self.stackarr[i][0], self.stackarr[i][1]
            if stacknum == numstack:
                return self.stackarr.pop(i)[0]
        raise ValueError


x = threestack(3)
x.push(1,1)
print(x.peek(1))
x.push(4,2)
print(x.pop(2))
