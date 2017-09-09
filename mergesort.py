# fn to merge two arrays
def merge(a, b):
	c = []
	while len(a) != 0 and len(b) != 0:
		if a[0] < b[0]:
			c.append(a[0])
			a.remove(a[0])
		else:
			c.append(b[0])
			b.remove(b[0])
	if len(a) == 0:
		c += b
	else:
		c+= a
	return c

# get the left and right, merge sort them then bring them back toghter
def merge_sort(array):
	if len(array) <= 1:
		return array
	else:
		mid = len(array)/2
		left = merge_sort(array[:mid])
		right = merge_sort(array[mid:])
		return merge(left, right)

print(merge_sort([1,2,3,4,5,6,5,4,3,2,1,2,3,4,5,6,6,7,8,9,8,0]))