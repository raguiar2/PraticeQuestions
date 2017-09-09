def subarray_zero(arr):
	total = 0
	sums = {}
	for i in range(len(arr)+1):
		if total in sums:
			sumval = sums[total]
		else:
			if i == len(arr):
				return []
			sumval = None
		if sumval is None:
			sums[total] = i
			total += arr[i]
		else:
			return arr[sums[total]:i]
	return []






print(subarray_zero([1,2,-5,1,2]))


print(subarray_zero([1,2,-5,1,2,-1]))

print(subarray_zero([1,-1,0,2]))
