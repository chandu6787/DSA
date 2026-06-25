class Solution:
    def possible(self,nums,threshold,num):
        sum=0
        for i in range(len(nums)):
            sum+=ceil(nums[i]/num)
        if sum<=threshold:
            return True
        else:
            return False
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low,high=1,max(nums)
        while low<=high:
            mid=(low+high)//2
            if self.possible(nums,threshold,mid):
                high=mid-1
            else:
                low=mid+1
        return low
        