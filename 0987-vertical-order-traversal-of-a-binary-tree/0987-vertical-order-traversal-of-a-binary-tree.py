# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque,defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        q=deque([(root,0,0)])
        cols=defaultdict(list)
        ans=[]
        min_col,max_col=0,0
        while q:
            node,row,col=q.popleft()
            cols[col].append((row,node.val))
            min_col=min(min_col,col)
            max_col=max(max_col,col)
            if node.left:
                q.append((node.left,row+1,col-1))
            if node.right:
                q.append((node.right,row+1,col+1))
        for c in range(min_col,max_col+1):
            cols[c].sort()
            ans.append([val for row,val in cols[c]])
        return ans
        