# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not head:
            return True
        if not root:
            return False
        
        a=self.helper(head,root)
        res=a or self.isSubPath(head,root.left) or self.isSubPath(head,root.right)
        return (res)
    
    def helper(self,head,root):
        if not head:
            return True
        if not root:
            return False
        else:
            lhelp=self.helper(head.next,root.left)
            rhelp=self.helper(head.next,root.right)
            x= lhelp or rhelp
            y= head.val == root.val
            return (x and y)