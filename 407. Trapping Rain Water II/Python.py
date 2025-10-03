# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])

        # Check whether a cell is inside the grid
        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n

        # Min-heap (priority queue) to always expand from the lowest boundary
        pq = []

        # Visited matrix to mark processed cells
        vis = [[False] * n for _ in range(m)]

        # Directions: right, left, down, up
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Step 1: Push all boundary cells into the heap
        for i in range(m):
            if i == 0 or i == m - 1:
                # top and bottom rows (all columns)
                for j in range(n):
                    heapq.heappush(pq, (heightMap[i][j], (i, j)))
                    vis[i][j] = True
            else:
                # leftmost and rightmost columns
                heapq.heappush(pq, (heightMap[i][0], (i, 0)))
                heapq.heappush(pq, (heightMap[i][n - 1], (i, n - 1)))
                vis[i][0] = True
                vis[i][n - 1] = True

        # Step 2: BFS with min-heap
        water = 0
        while pq:
            height, (i, j) = heapq.heappop(pq)  # always take lowest boundary

            for dx, dy in dirs:
                nRow, nCol = i + dx, j + dy

                if isValid(nRow, nCol) and not vis[nRow][nCol]:
                    nHeight = heightMap[nRow][nCol]

                    # If neighbor is lower than current boundary,
                    # water can be trapped (difference in height)
                    water += max(0, height - nHeight)

                    # The new boundary height becomes max of current height & neighbor
                    heapq.heappush(pq, (max(height, nHeight), (nRow, nCol)))

                    # Mark visited
                    vis[nRow][nCol] = True

        return water
