class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l < 2:
            return l
        chars = set()
        max_len = 1
        head = 0
        tail = 1
        chars.add(s[head])
        while head < l and tail < l:
            if s[tail] not in chars:
                if tail - head + 1 > max_len:
                    max_len = tail - head + 1
                chars.add(s[tail])
            else:
                while s[head] != s[tail]:
                    chars.remove(s[head])
                    head += 1
                head += 1
            tail += 1
        
        return max_len