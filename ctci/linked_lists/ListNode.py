class ListNode():
    def __init__(self,data=0):
        self.next = None
        self.data = data
    def append_to_tail(self,node):
        if not self.next:
            self.next = node
        temp = self.next
        while temp.next:
            temp = temp.next
        temp.next = node

