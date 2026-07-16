class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        contained_zero = False
        zero_ind = None
        for i,n in enumerate(nums):
            if n == 0:
                if contained_zero:
                    return [0] * len(nums)
                contained_zero = True
                zero_ind = i
            else:
                prod *= n
        if contained_zero:
            final_list = [0] * len(nums)
            final_list[zero_ind] = prod
            return final_list
        else:
            return [int(prod/x) for x in nums]
            
