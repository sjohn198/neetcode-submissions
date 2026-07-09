class Solution:
    def searchRow(self, lst, target):
        left = 0
        right = len(lst) - 1
        count = 0
        while left <= right:
            count += 1
            if count == 8:
                #print("fucked up")
                return False
            mid = (right + left) // 2
            #print(right, left, mid)
            if lst[mid] == target:
                return True
            elif lst[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [[]]:
            return false
        col_len = len(matrix)
        row_len = len(matrix[0])
        #binary search to identify row and then binary search to identify value
        top = 0
        bottom = col_len - 1

        while top <= bottom:
            #print(top, bottom)
            mid_col = (bottom + top) // 2
            if matrix[mid_col][0] <= target and matrix[mid_col][-1] >= target:
                #found row
                return self.searchRow(matrix[mid_col], target)
            elif matrix[mid_col][0] > target:
                #print("look lower")
                bottom = mid_col - 1
                #print("new bot", bottom)
            elif matrix[mid_col][-1] < target:
                #print("look higher")
                top = mid_col + 1

        return False