class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                nums[i]=-1
        mp={}
        maxlen=0
        prefix_sum=0
        for i in range(n):
            prefix_sum+=nums[i]
            if prefix_sum==0:
                maxlen=max(i+1,maxlen)
            if prefix_sum in mp:
                maxlen=max(maxlen,i-mp[prefix_sum])
            if prefix_sum not in mp:
                mp[prefix_sum]=i
        return maxlen

        