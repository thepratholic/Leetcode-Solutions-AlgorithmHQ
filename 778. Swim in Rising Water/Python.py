# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Visited matrix to track visited cells
        vis = [[False] * n for _ in range(n)]

        # Min-heap (priority queue) to always explore the smallest possible elevation first
        pq = []

        # 4-directional moves (Right, Up, Down, Left)
        dirs = [(0, 1), (-1, 0), (1, 0), (0, -1)]

        # Helper function to check boundaries
        def isValid(i, j):
            return 0 <= i < n and 0 <= j < n

        # Start at (0, 0), initial water level equals the elevation at the starting cell
        t = grid[0][0]

        # Push starting cell into min-heap → (time/elevation, (i, j))
        heapq.heappush(pq, (t, (0, 0)))
        vis[0][0] = True

        # ------------------------------------
        # Dijkstra-like traversal (using min-heap)
        # ------------------------------------
        while pq:
            # Pop the cell with the smallest current elevation/time
            cur_t, (i, j) = heapq.heappop(pq)

            # If we’ve reached the bottom-right cell → return the time
            if i == n - 1 and j == n - 1:
                return cur_t

            # Explore all 4 neighboring cells
            for dx, dy in dirs:
                nRow, nCol = i + dx, j + dy

                # Move only to valid & unvisited neighbors
                if isValid(nRow, nCol) and not vis[nRow][nCol]:
                    nxt = grid[nRow][nCol]

                    # The water level must be at least as high as the current path max elevation
                    # So take the maximum of current time and next cell’s height
                    heapq.heappush(pq, (max(nxt, cur_t), (nRow, nCol)))

                    # Mark neighbor as visited
                    vis[nRow][nCol] = True

        # If destination is unreachable (theoretically never happens in this problem)
        return -1
