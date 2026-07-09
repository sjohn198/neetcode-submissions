class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        dp = [-1] * (amount + 1)

        i = 1
        while i <= amount:
            min_count = float('inf')
            for coin in coins:
                if coin == i:
                    dp[i] = 1
                    min_count = 1
                elif coin < i:
                    cur_val = min_count
                    if dp[i - coin] != -1:
                        cur_val = 1 + dp[i - coin]
                    if cur_val < min_count:
                        min_count = cur_val
            if min_count != float('inf'):
                dp[i] = min_count

            i += 1
        return dp[-1]
