class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      val_map = {}

      for i in range(len(nums)):
        if nums[i] in list(val_map.keys()):
            return [val_map[nums[i]], i]
        val_map[target - nums[i]] = i
        