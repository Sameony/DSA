class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not (headA and headB):
            return None
        curr1,curr2=headA,headB
        while curr1 != curr2:
            curr1=headB if not curr1 else curr1.next
            curr2=headA if not curr2 else curr2.next
        return curr1
#O(m+n) run time and O(1)
#op bolte....switching heads solves the irregular length problem

#another solution will be concatenating the lists and then searching for a loop.if loop -> they do intersect.

class Solution(object):
    def getIntersectionNode(self, A, B):
        if not A or not B: return None

        # Concatenate A and B
        last = A
        while last.next: last = last.next
        last.next = B

        # Find the start of the loop
        fast = slow = A
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                fast = A
                while fast != slow:
                    slow, fast = slow.next, fast.next
                last.next = None
                return slow

        # No loop found
        last.next = None
        return None