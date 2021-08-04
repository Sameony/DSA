# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            L_sum=self.countNodes(root.left)
            R_sum=self.countNodes(root.right)
            return 1+L_sum+R_sum