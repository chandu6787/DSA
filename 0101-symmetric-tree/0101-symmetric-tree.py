# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root.left and not root.right:
            return True
        def helper(lsub,rsub):
            if not lsub and not rsub:
                return True
            if not lsub or not rsub:
                return False
            if lsub.val!=rsub.val:
                return False
            return helper(lsub.left,rsub.right) and helper(lsub.right,rsub.left)
        return helper(root.left,root.right)
