# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        ans=float('-inf')
        def helper(node):
            nonlocal ans
            if not node:
                return 0
            ls=max(0,helper(node.left))
            rs=max(0,helper(node.right))
            ans=max(ans,node.val+ls+rs)
            return node.val+max(ls,rs)
        helper(root)
        return ans