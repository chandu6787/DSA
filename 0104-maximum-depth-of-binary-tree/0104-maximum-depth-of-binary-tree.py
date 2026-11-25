# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def height(root):
            if not root:
                return 0
            lH=height(root.left)
            rH=height(root.right)
            return 1+max(lH,rH)
        return height(root)