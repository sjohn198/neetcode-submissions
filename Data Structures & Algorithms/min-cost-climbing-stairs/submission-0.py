class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)

        dp[-1] = 0
        dp[-2] = cost[-1]

        i = len(dp) - 3

        while i >= 0:
            dp[i] = min(dp[i + 1], dp[i + 2]) + cost[i]
            i -= 1

        return min(dp[0], dp[1])