from pprint import pprint


class Sudoku:

    def __init__(self, grid):
        self.grid = grid

    def is_that_a_legal_move(self, x, y, n):
        for i in range(0, 9):
            if self.grid[i][y] == n:
                return False
        for i in range(0, 9):
            if self.grid[x][i] == n:
                return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[x0+i][y0+j] == n:
                    return False
        return True

    def solution_stream(self):
        for y in range(9):
            for x in range(9):
                if self.grid[x][y] == 0:
                    for n in range(1, 10):
                        if self.is_that_a_legal_move(x, y, n):
                            self.grid[x][y] = n
                            yield from self.solution_stream()
                            self.grid[x][y] = 0
                    return
        yield self.grid


S = Sudoku(grid=[
    [5, 0, 0, 0, 8, 0, 0, 4, 9],
    [0, 0, 0, 5, 0, 0, 0, 3, 0],
    [0, 6, 7, 3, 0, 0, 0, 0, 1],
    [1, 5, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 8],
    [7, 0, 0, 0, 0, 4, 1, 5, 0],
    [0, 3, 0, 0, 0, 2, 0, 0, 0],
    [4, 9, 0, 0, 5, 0, 0, 0, 3]]
)

for g in S.solution_stream():
    pprint(g)
