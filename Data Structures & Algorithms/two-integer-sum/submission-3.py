class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      val_map = {}

      for i, num in enumerate(nums):
        if num in list(val_map.keys()):
            return [val_map[num], i]
        val_map[target - num] = i
        