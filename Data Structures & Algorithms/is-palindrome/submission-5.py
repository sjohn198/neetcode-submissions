class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return False
        real_s = ""
        for ch in s:
            if ch.isalnum():
                real_s += ch.lower()
        print(real_s)
        front = 0
        back = len(real_s) - 1
        mid = len(real_s) // 2

        while back >= mid:
            print(front, back)
            if real_s[front] != real_s[back]:
                return False
            front += 1
            back -= 1
            
        return True