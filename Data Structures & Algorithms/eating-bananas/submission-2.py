import math
class Solution:
    def calcHours(self, piles: List[int], speed: int) -> int:
        hours = 0
        for p in piles:
            hours += math.ceil(p / speed)
        return hours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = max(piles)
        possible_speeds = range(1, min_speed + 1)
        left = 0
        right = min_speed - 1
        while left <= right:
            mid = (left + right) // 2
            cur_rate = possible_speeds[mid]
            hours = self.calcHours(piles, cur_rate)
            print(cur_rate, hours)
            if hours > h:
                left = mid + 1
            else:
                print(hours)
                if cur_rate < min_speed:
                    min_speed = cur_rate
                right = mid - 1
        return min_speed

