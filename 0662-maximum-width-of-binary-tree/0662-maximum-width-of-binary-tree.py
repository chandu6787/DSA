# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root.left and not root.right:
            return 1
        q=deque([(root,0)])
        ans=0
        while q:
            n=len(q)
            mini=q[0][1]
            first,last=0,0
            for i in range(n):
                node,idx=q.popleft()
                idx-=mini
                if i==0:
                    first=idx
                if i==n-1:
                    last=idx
                if node.left:
                    q.append((node.left,2*idx+1))
                if node.right:
                    q.append((node.right,2*idx+2))
            ans=max(ans,last-first+1)
        return ans
                