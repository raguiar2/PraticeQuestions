def search_rotated_array_helper(arr,elem,low,high):
	mid = (low+high)/2
	if low <= high:
		if arr[mid] == elem:
			return elem
		if arr[low] <= arr[mid]:
			if (elem >= arr[low] and elem <= arr[mid]):
				return search_rotated_array_helper(arr,elem,low,mid-1)
			return search_rotated_array_helper(arr,elem,mid+1,high)
		elif arr[high] >= arr[mid]:
			if elem >= arr[mid] and elem <= arr[high]:
				return search_rotated_array_helper(arr,elem,mid+1,high)
			return search_rotated_array_helper(arr,elem,low,mid-1)

def search_rotated_array(arr, elem):
	return search_rotated_array_helper(arr,elem,0,len(arr)-1)



print(search_rotated_array([30, 40, 50, 10, 20],10))

print(search_rotated_array([30, 40, 50, 10, 20],30))

print(search_rotated_array([30, 40, 50, 10, 20],4000))