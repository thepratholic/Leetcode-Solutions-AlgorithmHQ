# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    UNGUARDED = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3

    # Depth-First Search to mark guarded cells
    def _dfs(self, row: int, col: int, grid: List[List[int]], direction: str) -> None:
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[0])
            or grid[row][col] == self.GUARD
            or grid[row][col] == self.WALL
        ):
            return  # Stop recursion if out of bounds or cell is a guard/wall

        grid[row][col] = self.GUARDED  # Mark cell as guarded

        # Continue marking cells in the same direction
        if direction == "U":
            self._dfs(row - 1, col, grid, "U")  # Up
        if direction == "D":
            self._dfs(row + 1, col, grid, "D")  # Down
        if direction == "L":
            self._dfs(row, col - 1, grid, "L")  # Left
        if direction == "R":
            self._dfs(row, col + 1, grid, "R")  # Right

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize the grid with all cells unguarded
        grid = [[self.UNGUARDED for _ in range(n)] for _ in range(m)]

        # Place guards on the grid
        for guard in guards:
            grid[guard[0]][guard[1]] = self.GUARD

        # Place walls on the grid
        for wall in walls:
            grid[wall[0]][wall[1]] = self.WALL

        # Mark cells as guarded by traversing in all directions from each guard
        for guard in guards:
            self._dfs(guard[0] - 1, guard[1], grid, "U")  # Up
            self._dfs(guard[0] + 1, guard[1], grid, "D")  # Down
            self._dfs(guard[0], guard[1] - 1, grid, "L")  # Left
            self._dfs(guard[0], guard[1] + 1, grid, "R")  # Right

        # Count the number of unguarded cells
        count = sum(row.count(self.UNGUARDED) for row in grid)
        return count


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/
