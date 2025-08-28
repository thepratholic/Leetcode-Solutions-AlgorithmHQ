# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List

class Solution:
    # Helper function to sort one diagonal of the matrix
    def f(self, i, j, asc, grid):
        n = len(grid)
        diagonal = []  # to store elements of the diagonal
        row, col = i, j

        # Step 1: Collect all elements of the diagonal starting from (i, j)
        while row < n and col < n:
            diagonal.append(grid[row][col])
            row += 1
            col += 1

        # Step 2: Sort the diagonal
        if asc:
            # If asc = True, sort in ascending order
            diagonal.sort()
        else:
            # If asc = False, sort in descending order
            diagonal.sort(reverse=True)

        # Step 3: Put back the sorted elements into the same diagonal
        row, col = i, j
        ptr = 0
        while row < n and col < n:
            grid[row][col] = diagonal[ptr]  # replace with sorted value
            row += 1
            col += 1
            ptr += 1

    # Main function to sort diagonals of matrix
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        # Step 1: Sort diagonals starting from top row (except first column)
        # These diagonals are sorted in ASCENDING order
        for j in range(1, n):
            self.f(0, j, True, grid)

        # Step 2: Sort diagonals starting from first column
        # These diagonals are sorted in DESCENDING order
        for i in range(n):
            self.f(i, 0, False, grid)

        # Return the modified grid
        return grid
