# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from collections import deque
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Number of rows
        n = len(mat)
        # Number of columns
        m = len(mat[0])

        # Queue for BFS
        q = deque()
        # Set to keep track of visited cells (row, col)
        vis = set()

        # Start from the top-left corner (0,0)
        q.append((0, 0)) 
        vis.add((0, 0)) # mark as visited
        level = 0  # to keep track of diagonal levels

        ans = []  # final result array

        # BFS traversal
        while q:
            length = len(q)   # number of nodes in the current level
            cur = []          # to store values of the current diagonal

            for _ in range(length):
                # Pop one cell from queue
                i, j = q.popleft()
                cur.append(mat[i][j])  # add matrix value to current diagonal

                # Right neighbor (same row, next column)
                if j + 1 < m and (i, j + 1) not in vis:
                    vis.add((i, j + 1))
                    q.append((i, j + 1))

                # Down neighbor (next row, same column)
                if i + 1 < n and (i + 1, j) not in vis:
                    vis.add((i + 1, j))
                    q.append((i + 1, j))

            # Zig-zag pattern: reverse elements on even levels
            if level & 1:   # odd level → keep as is
                ans.extend(cur)
            else:           # even level → reverse the collected diagonal
                cur = cur[::-1]
                ans.extend(cur)

            level += 1  # move to next diagonal

        return ans
