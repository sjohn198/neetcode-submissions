class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
        print(q)
        while q != []:
            cur_node = q.pop(0)
            #print(cur_node)
            i = cur_node[0]
            j = cur_node[1]
            cur_distance = grid[cur_node[0]][cur_node[1]] + 1
            #print(cur_distance)
            if i > 0:
                if grid[i-1][j] == 2147483647:
                    #print("up is free")
                    grid[i-1][j] = cur_distance
                    q.append((i-1, j))
            if j > 0:
                if grid[i][j-1] == 2147483647:
                    #print(f"left is free, {i}, {j-1}, {grid[i][j-1]}")
                    grid[i][j-1] = cur_distance
                    q.append((i, j-1))
            if i < len(grid) - 1:
                if grid[i+1][j] == 2147483647:
                    #print("down is free")
                    grid[i+1][j] = cur_distance
                    q.append((i+1, j))
            if j < len(grid[0]) - 1:
                if grid[i][j+1] == 2147483647:
                    #print("right is free")
                    grid[i][j+1] = cur_distance
                    q.append((i, j+1))