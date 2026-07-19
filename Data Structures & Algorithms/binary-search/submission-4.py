class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            n = nums[mid]
            # print(right, left, mid)
            #print(n)
            if n == target:
                return mid
            elif n > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1