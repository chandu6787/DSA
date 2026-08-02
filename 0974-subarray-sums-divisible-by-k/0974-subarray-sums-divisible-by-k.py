class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp={0:1}
        n=len(nums)
        ans=0
        prefix_sum=0
        for i in range(n):
            prefix_sum+=nums[i]
            rem=prefix_sum%k
            ans+=mp.get(rem%k,0)
            mp[rem]=mp.get(rem,0)+1
        return ans
        