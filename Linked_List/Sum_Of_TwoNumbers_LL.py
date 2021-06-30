class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    fin = cur =ListNode(0)
    c = 0
    while l1 or l2 or c:
        if l1:
            c += l1.val
            l1 = l1.next
        if l2:
            c += l2.val
            l2 = l2.next
        cur.next = ListNode(c%10)
        cur = cur.next
        c //=10
    return fin.next