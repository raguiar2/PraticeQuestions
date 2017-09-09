from Queue import PriorityQueue

class SortedValue():
	def __init__(self, value, listidx, listnum):
		self.value = value
		self.listidx = listidx
		self.listnum = listnum
	def __str__(self):
		return'value:' + str(self.value) + ' listidx:' +  str(self.listidx) + ' listnum: ' +  str(self.listnum)
	def __cmp__(self, other):
		if other.value < self.value:
			return 1
		elif other.value > self.value:
			return -1
		else:
			return 0
# time complexity is kn * log(kn)
def merge_k_lists(lists):
	pq = PriorityQueue()
	result = []
	for i, lst in enumerate(lists):
		if len(lst) > 0:
			firstval = SortedValue(lst[0],0,i)
			# priority is value, store index of array and number of array as a tuple 
			# might be good to instantiate as a class
			pq.put(firstval, firstval.value)
	while not pq.empty():
		val = pq.get()
		value = val.value
		listidx = val.listidx
		listnum = val.listnum
		result.append(value)
		originlst = lists[listnum]
		if listidx + 1 < len(originlst):
			nextval = SortedValue(originlst[listidx+1],listidx+1, listnum)
			pq.put(nextval, nextval.value)
	return result






lists = [[1,2,3],[3,4,5],[6,7,8]]
print(merge_k_lists(lists))
lists = [[1,2],[3,4]]
print(merge_k_lists(lists))