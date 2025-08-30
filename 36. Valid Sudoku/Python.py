# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each row, column, and 3x3 sub-box will have its own set
        rows = defaultdict(set)   # maps row index → set of seen numbers
        cols = defaultdict(set)   # maps col index → set of seen numbers
        boxes = defaultdict(set)  # maps (row//3, col//3) → set of seen numbers

        # Traverse every cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                
                # Skip empty cells represented by '.'
                if board[r][c] == '.':
                    continue

                # Check if the number already exists in the same row, col, or 3x3 box
                if (
                    board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in boxes[(r // 3, c // 3)]
                ):
                    return False  # Invalid Sudoku

                # Otherwise, add the number to the corresponding sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])

        # If no conflicts were found, the Sudoku board is valid
        return True