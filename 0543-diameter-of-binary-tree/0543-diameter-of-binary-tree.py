# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        diameter=0
        def helper(node):
            nonlocal diameter
            if not node:
                return 0
            leftH=helper(node.left)
            rightH=helper(node.right)
            diameter=max(diameter,leftH+rightH)
            return 1+max(leftH,rightH)
        helper(root)
        return diameter

        