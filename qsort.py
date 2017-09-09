import sys

def partition(lst, low, high):
	low_elem = low - 1 
	pivot = lst[high]
	for i in range(low, high):
		if lst[i] <= pivot:
			low_elem += 1
			lst[low_elem], lst[i] = lst[i], lst[low_elem]
	lst[low_elem+1], lst[high] = lst[high], lst[low_elem+1]
	return low_elem + 1




def qsort(lst, low, high):
	if low < high:
		pi = partition(lst, low, high)
		qsort(lst, low, pi-1)
		qsort(ls, pi+1, high)
	return lst



ls = [0,2,3,4,1,0,2,34,5,6,5]

print(qsort(ls, 0, len(ls)-1))