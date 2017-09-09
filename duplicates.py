def duplicates(arr):
	res = set()
	arrlen = len(arr)
	for i in range(len(arr)):
		idx = abs(arr[i])
		index = idx - 1
		if arr[index] < 0:
			res.add(arr[i])
		else:
			arr[index] = arr[index] * -1
	return res

def kth_most_frequent(words,k):
	from collections import defaultdict
	counts= defaultdict(int)
	for word in words:
		counts[word] += 1
	values = [(val[0],val[1]) for val in  counts.items()]
	if k > len(values):
		return None
	values.sort(key = lambda x: x[1])
	return values[-k][0]

def consecutive_numbers(arr):
	values = set()
	for val in arr:
		values.add(val)
	maxlen = 0
	for val in values:
		# skip if it contains value to the left
		if i-1 in values:
			continue
		length = 0
		while i+1 in values:
			i += 1
			length += 1
			maxlen = max(maxlen,length)

