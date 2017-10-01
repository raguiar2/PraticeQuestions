def longest_arithmatic(arr):
	if arr == []:
		return 0
	if len(arr) == 1:
		return 1
	maxlen = 1
	currlen = 1
	step = arr[1]-arr[0]
	for i in range(1,len(arr)):
		if arr[i-1]+step == arr[i]:
			currlen += 1
			maxlen = max(maxlen,currlen)
		else:
			step = arr[i] - arr[i-1]
			currlen = 2
	return maxlen
