class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            print(left, right, mid)
            if nums[mid] == target:
                return mid
            if nums[left] < nums[mid]:
                #in left sorted portion
                if (target < nums[mid] and target < nums[left]) or target > nums[mid]:
                    #it must be to the right
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                #in right sorted portion
                if target > nums[mid] and target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
                
                

        return -1