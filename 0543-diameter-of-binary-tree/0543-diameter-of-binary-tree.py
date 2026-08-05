# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recu(self,root):
     if root is None:
        return 0
     left = self.recu(root.left)
     right = self.recu(root.right)
     self.ans=max(self.ans,left+right)
     return 1 + max(left, right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        self.recu(root)
        return self.ans
        