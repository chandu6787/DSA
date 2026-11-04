# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        ans=float('-inf')
        def helper(node):
            nonlocal ans
            if not node:
                return 0
            leftS=max(0,helper(node.left))
            rightS=max(0,helper(node.right))
            ans=max(ans,node.val+leftS+rightS)
            return node.val+max(leftS,rightS)
        helper(root)
        return ans
