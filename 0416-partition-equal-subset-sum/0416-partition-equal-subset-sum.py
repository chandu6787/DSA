class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ=sum(nums)
        n=len(nums)
        if summ%2==1:
            return False
        else:
            target=summ//2
            dp=[[False]*(target+1) for _ in range(n+1)]
            for i in range(n+1):
                dp[i][0]=True
            for i in range(1,n+1):
                for j in range(1,target+1):
                    if nums[i-1]<=j:
                        take=dp[i-1][j-nums[i-1]]
                        not_take=dp[i-1][j]
                        dp[i][j]=take or not_take
                    else:
                        dp[i][j]=dp[i-1][j]
            return dp[n][target]
        return -1
        
        