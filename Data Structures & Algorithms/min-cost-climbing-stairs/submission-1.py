class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost))
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]

        i = len(cost) - 3
        while i >= 0:
            print(f"i: {i}, dp:{dp}")
            dp[i] = min(cost[i] + dp[i+2], cost[i] + dp[i+1])
            i -= 1
        return min(dp[0],dp[1])
        
