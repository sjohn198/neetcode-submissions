class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[-2] = 1
        dp[-1] = 1

        i = len(dp) - 3
        while i >= 0:
            dp[i] = dp[i + 1] + dp[i + 2]
            i -= 1
        return dp[0]