class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []
        first_num = set()
        n_sorted = sorted(nums)
        triplets = []
        for i in range(len(n_sorted)):
            target = n_sorted[i]
            if i == len(n_sorted) - 2:
                return triplets
            if target in first_num:
                continue
            left = i + 1
            right = len(n_sorted) - 1
            while left < right:
                if n_sorted[left] + n_sorted[right] + target == 0:
                    triplets.append([target, n_sorted[left], n_sorted[right]])
                    first_num.add(target)
                    cur_left = n_sorted[left]
                    while left < right and n_sorted[left] == cur_left:
                        left += 1
                    cur_right = n_sorted[right]
                    while left < right and n_sorted[right] == cur_right:
                        right -= 1
                elif n_sorted[left] + n_sorted[right] + target > 0:
                    right -= 1
                else:
                    left += 1
        