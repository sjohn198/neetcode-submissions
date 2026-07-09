class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for n in nums:
            prod *= n
        
        output = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                nums2 = nums.copy()
                nums2.pop(i)
                prod2 = 1
                for n in nums2:
                    prod2 *= n
                output[i] = prod2
            else:
                output[i] = int(prod / nums[i])
        
        return output
