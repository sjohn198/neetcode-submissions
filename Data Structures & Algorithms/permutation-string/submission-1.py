class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        ref = sorted(s1)
        
        head = 0
        tail = 0

        while head < len(s2):
            if tail - head + 1 == len(s1) and sorted(s2[head:tail+1]) == ref:
                return True
            elif tail - head + 1 > len(s1):
                head += 1
            else:
                tail += 1
        return False
                