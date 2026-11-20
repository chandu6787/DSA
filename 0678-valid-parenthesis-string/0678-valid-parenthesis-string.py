class Solution:
    def checkValidString(self, s: str) -> bool:
        minL,maxL=0,0
        n=len(s)
        for i in range(n):
            if s[i]=='(':
                minL+=1
                maxL+=1
            elif s[i]==')':
                minL-=1
                maxL-=1
            else:
                minL-=1
                maxL+=1
            if minL<0:
                minL=0
            if maxL<0:
                return False
        return minL==0
        