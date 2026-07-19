class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        zipped = zip(position, speed)
        zipped = sorted(zipped, key=lambda x: x[0])[::-1]
        
        stack = []
        for (p, s) in zipped:
            ttt = (target - p) / s
            stack.append(ttt)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)