class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        cookiesLen=len(s)
        greedLen=len(g)
        g.sort()
        s.sort()
        cp=0
        gp=0
        while cp<cookiesLen and gp<greedLen:
            if g[gp]<=s[cp]:
                gp+=1
            cp+=1
        return gp
        