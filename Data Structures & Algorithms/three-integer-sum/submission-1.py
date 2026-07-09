class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        first_nums = set()
        sort_nums = sorted(nums)
        triplets = []
        for i in range(len(sort_nums)):
            val = sort_nums[i]
            if i == len(sort_nums) - 2:
                return triplets
            if val in first_nums:
                continue
            #two sum 2
            left = i + 1
            right = len(sort_nums) - 1
            while left < right:
                if sort_nums[left] + sort_nums[right] + val == 0:
                    triplets.append([val, sort_nums[left], sort_nums[right]])
                    first_nums.add(val)
                    cur_left = sort_nums[left]
                    while left < right and sort_nums[left] == cur_left:
                        left += 1
                    cur_right = sort_nums[right]
                    while left < right and sort_nums[right] == cur_right:
                        right -= 1
                elif sort_nums[left] + sort_nums[right] + val > 0:
                    right -= 1
                else:
                    left += 1