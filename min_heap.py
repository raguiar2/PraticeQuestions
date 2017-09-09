class minHeap():
	def __init__(self):
		self.heaplist = [0]
		self.heapsize = 0
	def perc_up(self,currentSize):
		while currentSize > 2:
			if self.heaplist[i] > self.heaplist[i//2]:
				self.heaplist[i], self.heaplist[i//2] = self.heaplist[i//2], self.heaplist[i]
			i = i //2
	def insert(self,num):
		self.heaplist.append(num)
		self.heapsize += 1
		self.perc_up(self.currentSize)
	def min_child(self,i):
		if i*2+1 > self.currentSize:
			return i * 2
		else:
			if self.heaplist < self.heaplist[i*2+1]:
				return i * 2
			else:
				return i*2+1
	def perc_down(self,i):
		while i * 2 <= self.currentSize:
			mc = self.minChild(i)
			if self.heaplist[i] > self.heaplist[mc]:
			    self.heaplist[i],  self.heaplist[mc] = self.heaplist[mc],  self.heaplist[i]
			i = mc
	def del_min(self):
		retval = self.heaplist[1]
		self.heaplist[1] = self.heaplist[self.currentSize]
		self.currentSize -= 1
		self.heaplist.pop()
		self.perc_down(1)
		return retval