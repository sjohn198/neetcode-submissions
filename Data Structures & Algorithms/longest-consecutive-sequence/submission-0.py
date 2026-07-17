class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        s = set(nums)
        max_len = 1
        for n in nums:
            if n - 1 not in s:
                i = 0
                length = 0
                while n + i in s:
                    length += 1
                    s.remove(n+i)
                    i += 1
                if length > max_len:
                    max_len = length
        
        return max_len
