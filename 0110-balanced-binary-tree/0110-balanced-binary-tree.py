# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        def check(node):
            if not node:
                return 0
            leftH=check(node.left)
            rightH=check(node.right)
            if leftH==-1 or rightH==-1:
                return -1
            if abs(leftH-rightH)>1:
                return -1
            return 1+max(leftH,rightH)
        if check(root)==-1:
            return False
        else:
            return True
        