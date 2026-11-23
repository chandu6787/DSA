# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not inorder or not preorder:
            return None
        root=TreeNode(preorder.pop(0))
        idx=inorder.index(root.val)
        root.left=self.buildTree(preorder,inorder[:idx])
        root.right=self.buildTree(preorder,inorder[idx+1:])
        return root
        