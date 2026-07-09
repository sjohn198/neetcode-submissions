class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = [0] * (len(nums) + 1)

        dp[0] = nums[0]
        dp[1] = nums[1]

        i = 2
        while i < len(nums):
            print(dp)
            print(nums[i - 1])
            print(i)
            if i - 3 < 0:
                dp[i] = nums[i] + dp[i - 2]
            else:
                dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
            i += 1
        
        
        return max(dp[-2], dp[-3])

        