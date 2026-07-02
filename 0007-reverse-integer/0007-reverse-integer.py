class Solution:
    def reverse(self, x: int) -> int:
        num=0
        n=False
        if x<0:
            n=True
            x=x*-1
        while x:
            rem=x%10
            num=num*10+rem
            x=x//10
        if n and num>=-(2**31) and num<=(2**31)-1:
            return -num
        elif n==False and num>=-(2**31) and num<=(2**31)-1:
            return num
        return 0
        
        

        