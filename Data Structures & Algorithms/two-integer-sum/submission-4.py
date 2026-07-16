class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      val_map = {}

      for i, num in enumerate(nums):
        if num in val_map:
            return [val_map[num], i]
        val_map[target - num] = i
        