class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        while left < right:
            mid = (right - left) // 2 + left
            n = nums[mid]
            # print(right, left, mid)
            #print(n)
            if right - left == 1:
                if nums[left] == target:
                    return left
                if nums[right] == target:
                    return right
                else:
                    return -1
            if n == target:
                return mid
            elif n > target:
                right = mid
            else:
                left = mid
        return -1