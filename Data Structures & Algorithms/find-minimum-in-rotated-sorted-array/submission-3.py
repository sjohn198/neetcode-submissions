class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            #print(left, right, mid)
            if nums[left] > nums[right]:
                if nums[mid] >= nums[left]:
                    left = mid + 1
                    if nums[left - 1] > nums[left]:
                        return nums[left]
                else:
                    right = mid
                    if nums[right - 1] > nums[right]:
                        return nums[right]
            else:
                return nums[left]