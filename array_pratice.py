# Given an unsorted array of size n containing the integers 1 through n 
# in random order with one element randomly replaced by 0, 
# determine the missing element most efficiently.

def missing_elem(arr):
	length = len(arr)
	total = 0
	for i in len(arr):
		total += i
	for elem in arr:
		total -= elem
	return total


# Given an unsorted array of size n containing objects with ids of 0 … n-1, 
# sort the array in place and in linear time. 
# Assume that the objects contain large members such as binary data, 
# so instantiating new copies of the objects is prohibitively expensive.

def inplace_sort(arr):
	for i in range(len(arr)):
		while arr[i] != i:
			swap = arr[i]
			arr[i],arr[swap] = arr[swap],arr[i]

	return arr

#Practice Question: Write an iterative binary search for integers.

def iter_binserach(arr,elem):
	low = 0
	high = len(arr)-1
	while low <= high:
		middle = (low+high)//2
		if arr[middle] == elem:
			return middle
		elif arr[middle] < elem:
			low = middle + 1
		else:
			high = middle - 1
	return -1 

# Sample Question: Given a sorted array of size n with n elements (array1) 
# and a sorted array of size 2n with n elements (array2), 
# merge them to get a sorted array of size 2n. Do this in linear time and in-place.

def inplace_merge(longer,shorter,m,n):
	insert = len(longer) - 1
	while m >= 0 and n >= 0:
		if longer[m] < shorter[n]:
			longer[insert] = shorter[n]
			n -= 1
		else:
			longer[insert] = longer[m]
			m -= 1
		insert -= 1
	while m >= 0:
		longer[insert] = longer[m]
		m -= 1
		insert -= 1
	while n >= 0:
		longer[insert] = shorter[n]
		n -= 1
		insert -= 1
	return longer


