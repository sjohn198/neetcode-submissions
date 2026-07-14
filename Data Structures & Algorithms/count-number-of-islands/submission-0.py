class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        islands = 0
        visited = set()

        def bfs(row, col):
            q = [(row, col)]
            while q != []:
                cur_node = q.pop(0)
                visited.add(cur_node)
                temp_row = cur_node[0]
                temp_col = cur_node[1]
                #print(cur_node)
                if temp_row > 0 and grid[temp_row - 1][temp_col] == "1" and (temp_row-1, temp_col) not in visited:
                    #print("up is free")
                    q.append((temp_row-1, temp_col))
                if temp_col > 0 and grid[temp_row][temp_col-1] == "1" and (temp_row, temp_col-1) not in visited:
                    #print("left is free")
                    q.append((temp_row, temp_col-1))
                if temp_row < len(grid) - 1 and grid[temp_row + 1][temp_col] == "1" and (temp_row+1, temp_col) not in visited:
                    #print("down is free")
                    q.append((temp_row+1, temp_col))
                if temp_col < len(grid[0]) - 1 and grid[temp_row][temp_col + 1] == "1" and (temp_row, temp_col+1) not in visited:
                    #print(f"right is free, {temp_row},{temp_col+1},{grid[temp_row][temp_col+1]}")
                    q.append((temp_row, temp_col+1))
            #print("end bfs")

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
                    
        
        return islands