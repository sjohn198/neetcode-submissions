class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #print(grid)
        if grid == []:
            return 0
        visited = set()
        max_area = 0

        def bfs(row, col) -> int:
            q = [(row, col)]
            grid[row][col] += 1
            area = 0
            while q != []:
                cur_node = q.pop(0)
                area += 1
                temp_row = cur_node[0]
                temp_col = cur_node[1]
                #print(cur_node)
                if temp_row > 0 and grid[temp_row - 1][temp_col] == 1:
                    #print("up is free")
                    q.append((temp_row-1, temp_col))
                    grid[temp_row-1][temp_col] += 1
                if temp_col > 0 and grid[temp_row][temp_col-1] == 1:
                    #print("left is free")
                    q.append((temp_row, temp_col-1))
                    grid[temp_row][temp_col-1] += 1
                if temp_row < len(grid) - 1 and grid[temp_row + 1][temp_col] == 1:
                    #print("down is free")
                    q.append((temp_row+1, temp_col))
                    grid[temp_row+1][temp_col] += 1
                if temp_col < len(grid[0]) - 1 and grid[temp_row][temp_col + 1] == 1:
                    #print(f"right is free, {temp_row},{temp_col+1},{grid[temp_row][temp_col+1]}")
                    q.append((temp_row, temp_col+1))
                    grid[temp_row][temp_col+1] += 1
                #print(grid)
            #print("end bfs")
            return area
        #print("for loop")
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    temp_area = bfs(i, j)
                    #print(temp_area)
                    if temp_area > max_area:
                        max_area = temp_area
                    
        
        return max_area