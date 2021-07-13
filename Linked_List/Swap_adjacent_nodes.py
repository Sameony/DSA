class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        curr1, curr1.next = self, head
        while curr1.next and curr1.next.next:
            a = curr1.next
            b = a.next
            curr1.next, b.next, a.next = b, a, b.next
            curr1 = a
        return self.next