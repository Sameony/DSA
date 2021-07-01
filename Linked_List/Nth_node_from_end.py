class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    if not head.next:
        return None        
    curr,prev=head,head
    c=-n
    while True:
        curr=curr.next
        if c<0:
            c+=1
        else:
            prev=prev.next
        if not curr.next:
            break
    if c<0:
        head=head.next
    else:
        prev.next=prev.next.next
    return head