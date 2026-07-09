class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = []
        for i in range(len(temperatures)):
            j = i + 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                j += 1
            if j == len(temperatures):
                results.append(0)
            else:
                results.append(j-i)
        return results