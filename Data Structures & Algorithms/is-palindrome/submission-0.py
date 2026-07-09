class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = "".join([c.lower() for c in s if c.isalnum()])
        head = 0
        tail = len(cleaned_str) - 1
        while head <= tail:
            if cleaned_str[tail] != cleaned_str[head]:
                return False
            head += 1
            tail -= 1
        return True