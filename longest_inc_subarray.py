
def longest_cont_inc_subarray(arr):
	maxlen = 1
	currlen = 1
	for i in range(len(arr)):
		currelem = arr[i]
		currlen = 1
		for j in range(i+1,len(arr)):
			if arr[j] > currelem:
				currelem = arr[j]
				currlen += 1
		maxlen = max(currlen,maxlen)
	return maxlen


def longest_inc_subarray(arr):
	seqs = [1] * len(arr)
	for n in range(len(arr)):
		for i in range(0,n):
			if arr[i] < arr[n]:
				seqs[n] = max(seqs[n], seqs[i] + 1)
	return max(seqs)

print(longest_inc_subarray([1,2,3]))
print(longest_inc_subarray([1,2,3,4,1,2,3,4,5,1]))
print(longest_inc_subarray([3,2,1]))
print(longest_inc_subarray([3,9,9, 6, 7, 8, 9]))
print(longest_inc_subarray([3,2,4, 6, 7, 8, 2]))

def longestConsecutive(self, nums):
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best