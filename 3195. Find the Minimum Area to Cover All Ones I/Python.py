# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # Number of rows
        n = len(grid)
        # Number of columns
        m = len(grid[0])

        # Initialize variables to track the extreme positions of '1's
        # max_row = the lowest row index containing a '1'
        # min_row = the highest row index containing a '1'
        # max_col = the rightmost column index containing a '1'
        # min_col = the leftmost column index containing a '1'
        max_row, min_row = -1, n
        max_col, min_col = -1, m

        # Traverse through the entire grid
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    # Update boundaries whenever we find a '1'
                    max_row = max(max_row, i)   # farthest down
                    min_row = min(min_row, i)   # farthest up
                    min_col = min(min_col, j)   # farthest left
                    max_col = max(max_col, j)   # farthest right

        # Calculate height and width of the bounding rectangle
        # (max_row - min_row) + 1 → total number of rows covered
        # (max_col - min_col) + 1 → total number of columns covered
        return ((max_row - min_row) + 1) * ((max_col - min_col) + 1)