class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)

        dp[-1] = nums[-1]
        dp[-2] = nums[-2]

        i = len(nums) - 3
        while i >= 0:
            dp[i] = max(dp[i+1], nums[i] + max(dp[i+2:]))
            i -= 1
        return max(dp[0], dp[1])
    

        