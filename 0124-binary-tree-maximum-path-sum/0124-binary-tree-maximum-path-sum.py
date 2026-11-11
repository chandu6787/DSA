# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        ans=float('-inf')
        def helper(root):
            nonlocal ans
            if not root:
                return 0
            leftsum=max(0,helper(root.left))
            rightsum=max(0,helper(root.right))
            ans=max(ans,root.val+leftsum+rightsum)
            return root.val+max(leftsum,rightsum)
        helper(root)
        return ans
        