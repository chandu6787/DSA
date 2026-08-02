class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp={0:1}
        prefix_sum=0
        ans=0
        n=len(nums)
        for i in range(n):
            prefix_sum+=nums[i]
            ans+=mp.get(prefix_sum-k,0)
            mp[prefix_sum]=mp.get(prefix_sum,0)+1
        return ans