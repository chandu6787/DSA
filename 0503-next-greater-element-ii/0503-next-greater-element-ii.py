class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N=len(nums)
        nge=[-1]*N

        for i in range(N):
            for j in range(i+1,i+N):
                ind=j%N
                if nums[ind]>nums[i]:
                    nge[i]=nums[ind]
                    break
        return nge
        