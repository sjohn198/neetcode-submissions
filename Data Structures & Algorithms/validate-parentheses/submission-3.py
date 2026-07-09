class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        open2close = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        opens = ["(", "[", "{"]
        closes = ["}", ")", "]"]
    
        mid = int(n / 2)

        open_stack = []
        for i, ch in enumerate(s):
            if ch in opens:
                open_stack.append(ch)
            else:
                try:
                    if ch != open2close[open_stack.pop()]:
                        return False
                except Exception:
                    return False

        return len(open_stack) == 0
