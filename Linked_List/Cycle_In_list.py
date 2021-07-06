#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#slow pointer fast pointer
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not (head):
            return False
        if not head.next:
            return False
        if not head.next.next:
            return False
        if head.next.next==head:
            return True
        curr, ahead=head,head
        while True:
            ahead=ahead.next.next
            curr=curr.next
            if not ahead.next:
                return False
            elif not ahead.next.next:
                return False
            elif curr==ahead:
                return True
            






#Let python do the except
def hasCycle(self, head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False


# for sys.getrefcount(head):

#1 ref comes from the calling of this function itself according to the documentation
#2 Refs from the object being created, compiled and stored for optimization
#1 ref from a node A's next
#1 ref comes from another node B's next [if this happens, then there is a cycle]

def hasCycle(self, head):
    while sys.getrefcount(head) < 5:
        head = head.next
    return bool(head)
