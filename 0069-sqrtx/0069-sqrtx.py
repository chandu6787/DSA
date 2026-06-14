class Solution:
    def mySqrt(self, x: int) -> int:
        low,high=1,x
        while low<=high:
            mid=(low+high)//2
            current_num_square=mid*mid
            if current_num_square<=x:
                ans=mid
                low=mid+1
            else:
                high=mid-1

        return high
        