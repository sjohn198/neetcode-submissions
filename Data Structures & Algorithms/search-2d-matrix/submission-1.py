class Solution:
    def searchRow(self, row: List[int], target: int) -> bool:
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            n = row[mid]
            if n == target:
                return True
            elif n > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in matrix:
            if r[0] <= target and r[-1] >= target:
                return self.searchRow(r, target)
        return False