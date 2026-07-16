class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        row = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                cur_cell = board[r][c]
                if cur_cell == ".":
                    continue
                if cur_cell in row[r] or cur_cell in cols[c] or cur_cell in squares[(r//3, c//3)]:
                    # print(cur_cell)
                    # print(r, c)
                    # print(row[r])
                    # print(cols[c])
                    # print(r//3, c//3)
                    # print(squares[(r//3, c//3)])
                    return False

                row[r] = row.get(r, set())
                row[r].add(cur_cell)
                cols[c] = cols.get(c, set())
                cols[c].add(cur_cell)
                squares[(r//3, c//3)] = squares.get((r//3, c//3), set())
                squares[(r//3, c//3)].add(cur_cell)
        return True