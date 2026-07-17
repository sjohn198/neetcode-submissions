class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return False
        real_s = ""
        for ch in s:
            if ch.isalnum():
                real_s += ch.lower()
            
        return real_s == real_s[::-1]