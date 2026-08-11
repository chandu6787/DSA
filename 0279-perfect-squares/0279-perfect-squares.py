class Solution:
    def numSquares(self, n: int) -> int:

        squares = []

        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        m = len(squares)

        dp = [[n + 1] * (n + 1) for _ in range(m + 1)]

        # 0 squares are needed to make 0
        for i in range(m + 1):
            dp[i][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if squares[i - 1] <= j:
                    take = 1 + dp[i][j - squares[i - 1]]
                    not_take = dp[i - 1][j]

                    dp[i][j] = min(take, not_take)

                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]