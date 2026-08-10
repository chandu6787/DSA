class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        summ=sum(nums)
        n=len(nums)
        if (summ+target)%2!=0 or abs(target)>summ:
            return 0
        goal=(summ+target)//2
        dp=[[0]*(goal+1) for _ in range(n+1)]
        dp[0][0]=1
        for i in range(1,n+1):
            for j in range(goal+1):
                if nums[i-1]<=j:
                    take=dp[i-1][j-nums[i-1]]
                    not_take=dp[i-1][j]
                    dp[i][j]=take+not_take
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][goal]
