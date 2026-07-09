class Solution:
    def dfs(self, i, nums, res, subset):
        if i >= len(nums):
            res.append(subset.copy())
            return

        subset.append(nums[i])
        self.dfs(i + 1, nums, res, subset)
        subset.pop()
        self.dfs(i + 1, nums, res, subset)
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        return self.dfs(0, nums, res, subset)