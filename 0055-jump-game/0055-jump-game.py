class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxInd=0
        n=len(nums)
        for i in range(n):
            if i>maxInd:
                return False
            maxInd=max(maxInd,i+nums[i])
        return True

        