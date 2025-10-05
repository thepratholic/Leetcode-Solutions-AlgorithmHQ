# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        result = []

        # visP -> cells reachable from Pacific Ocean
        # visA -> cells reachable from Atlantic Ocean
        visP = [[False] * n for _ in range(m)]
        visA = [[False] * n for _ in range(m)]

        # Queues for BFS (one for each ocean)
        pq, aq = deque(), deque()

        # ---------------------------
        # Pacific Ocean borders (top & left)
        # ---------------------------
        for i in range(m):
            pq.append((i, 0))        # left border
            visP[i][0] = True

        for j in range(n):
            pq.append((0, j))        # top border
            visP[0][j] = True

        # ---------------------------
        # Atlantic Ocean borders (bottom & right)
        # ---------------------------
        for i in range(m):
            aq.append((i, n - 1))    # right border
            visA[i][n - 1] = True

        for j in range(n):
            aq.append((m - 1, j))    # bottom border
            visA[m - 1][j] = True

        # Helper to check if coordinates are valid
        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n

        # Directions (Up, Right, Down, Left)
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # ---------------------------
        # BFS function
        # ---------------------------
        # From the ocean borders, move inward to cells that are equal or higher in height
        # Because water can flow from high → low, so we reverse the flow:
        # start from ocean and move to cells that can send water into the ocean
        def bfs(q, vis):
            while q:
                i, j = q.popleft()

                for dx, dy in dirs:
                    nRow, nCol = i + dx, j + dy

                    # Move to neighbor only if:
                    # 1. inside grid
                    # 2. not visited yet
                    # 3. neighbor height >= current height (so water can flow down to current)
                    if isValid(nRow, nCol) and not vis[nRow][nCol] and heights[nRow][nCol] >= heights[i][j]:
                        vis[nRow][nCol] = True
                        q.append((nRow, nCol))

        # Run BFS for both oceans
        bfs(pq, visP)
        bfs(aq, visA)

        # ---------------------------
        # Collect cells reachable by both oceans
        # ---------------------------
        for i in range(m):
            for j in range(n):
                if visP[i][j] and visA[i][j]:
                    result.append((i, j))

        return result
