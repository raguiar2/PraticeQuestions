def binsearch_missing(arr,low,high,dist):
	if low <= high:
		middle = (low+high)/2
		if middle == len(arr):
			return arr[middle] + dist
		elif arr[middle] < arr[middle+1]+dist:
			return arr[middle] + dist
		if middle == 0:
			return arr[0] - dist
		elif arr[middle] != dist +  arr[middle-1]:
			return dist +  arr[middle-1]
		if arr[middle] <= arr[0] + (middle*dist):
			binsearch_missing(arr,middle+1,high,dist)
		else:
			binsearch_missing(arr,low,middle-1,dist)



def find_missing(arr):
	dist = (arr[-1]-arr[0])/len(arr)
	binsearch_missing(arr,0,len(arr)-1,dist)


