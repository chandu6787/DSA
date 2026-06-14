import math
class Solution:
    def checkThreshold(self,nums,number,threshold):
        sum=0
        for num in nums:
            sum+=math.ceil(num/number)
        if sum<=threshold:
            return True
        else:
            return False
            
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low,high=1,max(nums)
        while low<=high:
            mid=(low+high)//2
            if self.checkThreshold(nums,mid,threshold)==True:
                high=mid-1
            else:
                low=mid+1
        return low

        