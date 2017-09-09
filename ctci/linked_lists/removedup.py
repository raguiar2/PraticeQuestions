from ListNode import ListNode


def remove_dups(head):
    seen = {}
    prev = None
    temp = head
    while temp:
        print("here")
        if temp.data in seen:
            if prev:
                prev.next = temp.next
        else:
            seen[temp.data] = True
            prev = temp
        temp = temp.next
        print(temp)
