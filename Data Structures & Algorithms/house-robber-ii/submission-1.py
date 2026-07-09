class Solution:
    def hr1(self, nums):
        if len(nums) < 3:
            return max(nums)
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = nums[1]

        i = 2
        while i < len(nums):
            if i - 3 < 0:
                dp[i] = dp[i - 2] + nums[i]
            else:
                dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
            i += 1
        return max(dp[-1], dp[-2])
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        return max(self.hr1(nums[:-1]), self.hr1(nums[1:]))