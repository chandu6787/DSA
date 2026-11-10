class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        n=len(g)
        m=len(s)
        g.sort()
        s.sort()
        i,j=0,0
        while i<n and j<m:
            if g[i]<=s[j]:
                i+=1
            j+=1
        return i