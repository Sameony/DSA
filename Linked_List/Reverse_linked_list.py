class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        if not head.next.next:
            c=head.next
            c.next=head
            head.next=None
            return c
        prev=None
        c1=head
        forw=c1.next
        while True:
            c1.next=prev
            prev=c1
            if forw:
                c1=forw
            else:
                break
            if c1.next:
                forw=c1.next
            else:
                forw=None
        return c1