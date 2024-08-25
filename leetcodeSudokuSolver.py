class Solution:
    def __init__(self):
        # Initialize constraints for rows, columns, and 3x3 sub-grids
        self.row = [[False] * 9 for _ in range(9)]
        self.col = [[False] * 9 for _ in range(9)]
        self.sec = [[False] * 9 for _ in range(9)]

    def solveSudoku(self, board):
        # Initialize constraints based on the given board
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j]) - 1
                    self.row[i][num] = self.col[j][num] = self.sec[
                      (i // 3) * 3 + (j // 3)][num] = True

        self.solve(board, 0, 0)

    def solve(self, board, r, c):
        if r == 9:
            return True

        if c == 9:
            return self.solve(board, r + 1, 0)

        if board[r][c] != ".":
            return self.solve(board, r, c + 1)

        for num in range(9):
            if (
                not (self.row[r][num]
                or  self.col[c][num]
                or self.sec[(r // 3) * 3 + (c // 3)][num])
            ):
                board[r][c] = str(num + 1)
                self.row[r][num] = self.col[c][num] = self.sec[
                  (r // 3) * 3 + (c // 3)][num] = True
                if self.solve(board, r, c + 1):
                    return True
                # Backtrack
                self.row[r][num] = self.col[c][num] = self.sec[
                  (r // 3) * 3 + (c // 3)][num] = False
                board[r][c] = "."

        return False
