def kadane(A):
    max_sum = 0
    max_so_far = 0
    max_start_idx = 0
    startidx = 0
    max_end_idx = -1
    for i in range(len(A)):
    	max_so_far = max_so_far + a[i]
    	if max_so_far > max_sum:
    		endidx = i
    	if max_so_far < 0:
    		max_so_far = 0
    		startidx = i + 1

kadane([1,2,3])
kadane([-1, -2, -3, -4])
kadane([3,-2,4])
kadane([1,-15,4])
