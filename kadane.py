def kadane(a):
    start = 0
    _start = 0
    tempstart =0
    end = -1
    max_so_far = 0
    max_ending_here = 0
    for i in range(len(a)):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0
            tempstart = i + 1
        if max_so_far < max_ending_here:
            start = tempstart
            end = i
    print(start,end)

kadane([1,2,3])
kadane([-1, 2, -3, -4,-99])
kadane([3,-2,4])
kadane([1,-15,4])
