

def longest_subarray(array, k):
    counts = {0:-1}
    maxlen, acc = 0,0 
    for i in range(len(array)):
        acc += array[i]
        counts[acc] = i
        if acc-k in counts:
            maxlen = max(maxlen, counts[acc-k] + 1)
        return maxlen


print(longest_subarray([1,2,-3], 0))
            
