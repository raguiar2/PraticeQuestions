class SetOfStacks(object):
	def __init__(self, maxelems):
		self.stacks = []
		self.maxelems = maxelems
	def push(self, elem):
		if not self.stacks:
			self.stacks.append([])
		laststack = self.stacks[-1]
		if(len(laststack)>=self.maxelems):
			newstack = []
			newstack.append(elem)
			self.stacks.append(newstack)
		else:
			laststack.append(elem)
	def pop(self):
		laststack = self.stacks[-1]
		lastelem = laststack.pop(-1)
		if not laststack:
			self.stacks.pop(-1)
		return lastelem


class MinStack(object):
	def __init__(self):
		self.stack = []
	def push(self, elem):
		if not self.stack:
			pair = (elem,elem)
		else:
			currmin = self.min()
			if elem < currmin:
				pair = (elem,elem)
			else: 
				pair = (elem, currmin)
		self.stack.append(pair)

	def pop(self):
		return self.stack.pop(-1)[0]

	def peek(self):
		return self.stack[-1][0]

	def min(self):
		lastelem = self.stack[-1]
		return lastelem[1]

x = MinStack()
x.push(2)
