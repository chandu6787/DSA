class Solution:
    def possible(self,nums,maxValue):
        noOfSplits=1
        Sum=0
        for i in range(len(nums)):
            if (nums[i]+Sum)<=maxValue:
                Sum+=nums[i]
            else:
                Sum=nums[i]
                noOfSplits+=1
        return noOfSplits

    def splitArray(self, nums: List[int], k: int) -> int:
        low,high=max(nums),sum(nums)
        while low<=high:
            mid=(low+high)//2
            if self.possible(nums,mid)<=k:
                high=mid-1
            else:
                low=mid+1
        return low

        