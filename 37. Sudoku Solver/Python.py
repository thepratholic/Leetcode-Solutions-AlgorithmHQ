# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(int(board[i][j]))
                    cols[j].add(int(board[i][j]))
                    boxes[(i // 3, j // 3)].add(int(board[i][j]))

        def f(i, j):
            if i == 9 and j == 0:
                return True

            if board[i][j] != '.':
                if j != 8:
                    return f(i, j + 1)
                else:
                    return f(i + 1, 0)

            for k in range(1, 10):
                if k not in rows[i] and k not in cols[j] and k not in boxes[(i // 3, j // 3)]:
                    rows[i].add(k)
                    cols[j].add(k)
                    boxes[(i // 3, j // 3)].add(k)

                    board[i][j] = str(k)

                    if j != 8:
                        if f(i, j + 1):
                            return True
                    else:
                        if f(i + 1, 0):
                            return True

                    rows[i].remove(k)
                    cols[j].remove(k)
                    boxes[(i // 3, j // 3)].remove(k)
                    board[i][j] = '.'

            return False

        f(0, 0)
