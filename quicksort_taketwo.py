

def partition(arr, low, high):
	pivotpt = arr[high]
	idx = low - 1
	for i in range(low,high):
		if arr[i] <= pivotpt:
			idx += 1
			arr[i], arr[idx] = arr[idx], arr[i]
	idx += 1
	arr[idx], arr[high] = arr[high], arr[idx]
	return idx

def qsort(arr,low,high):
	if low < high:
		pivot = partition(arr, low, high)
		qsort(arr,pivot+1, high)
		qsort(arr,low, pivot-1)

array = [1,4,5,6,7,7,8,2,3,4,2,3,4]
qsort(array,0,len(array)-1)
print(array)