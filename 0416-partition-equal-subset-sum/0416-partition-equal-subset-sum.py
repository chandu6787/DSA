class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum=sum(nums)
        target_sum=int(total_sum/2)
        N=len(nums)
        if total_sum%2==1:
            return False
        else:
            dp=[[False for _ in range(target_sum+1)]for _ in range(N+1)]
            for i in range(0,N+1):
                dp[i][0]=True
            for i in range(1,N+1):
                for j in range(1,target_sum+1):
                    current_value=nums[i-1]
                    if current_value<=j:
                        take=dp[i-1][j-current_value]
                        not_take=dp[i-1][j]
                        dp[i][j]=take or not_take
                    else:
                        dp[i][j]=dp[i-1][j]
            return dp[N][target_sum]
        return -1

        