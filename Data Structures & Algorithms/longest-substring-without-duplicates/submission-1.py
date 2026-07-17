class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        max_len = 1
        sub_set = set()

        head = 0
        tail = 1
        sub_set.add(s[head])
        while tail < len(s):
            if s[tail] in sub_set:
                while s[head] != s[tail]:
                    sub_set.remove(s[head])
                    head += 1
                head += 1
                tail += 1
            else:
                sub_set.add(s[tail])
                tail += 1
                if tail - head > max_len:
                    max_len = tail - head

        return max_len
