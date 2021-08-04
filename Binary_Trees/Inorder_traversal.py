# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        x=[]
        self.helpme(root,x)
        return x
    def helpme(self,root,x):
        if root:
            self.helpme(root.left,x)
            x.append(root.val)
            self.helpme(root.right,x)