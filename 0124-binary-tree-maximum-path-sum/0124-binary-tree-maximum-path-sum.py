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
      left = max(0,self.recu(root.left))
      right = max(0,self.recu(root.right))
      self.ans=max(self.ans,left+right+root.val)
      return root.val+max(left,right)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=float('-inf')
        self.recu(root)
        return self.ans
        