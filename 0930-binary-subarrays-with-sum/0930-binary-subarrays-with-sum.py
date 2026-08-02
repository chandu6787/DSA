class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mp={0:1}
        n=len(nums)
        prefix_sum=0
        ans=0
        for i in range(n):
            prefix_sum+=nums[i]
            ans+=mp.get(prefix_sum-goal,0)
            mp[prefix_sum]=mp.get(prefix_sum,0)+1
        return ans

        