class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        stack = []
        open2close = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        openers = set(list(open2close.keys()))
        for ch in s:
            if ch in openers:
                stack.append(ch)
            else:
                if stack == []:
                    return False
                compare = stack.pop(-1)
                if open2close[compare] != ch:
                    return False
        return len(stack) == 0