
def kth_to_last(head,k):
    temp = head
    length = 0
    while temp:
        length += 1
        temp = temp.next
    iterations = length-k
    temp = head
    for i in range(iterations):
        temp = temp.next
    return temp


