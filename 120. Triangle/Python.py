# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        n = len(tri)   # number of rows in triangle

        # dp[i][j] will store the minimum path sum starting from tri[i][j]
        dp = [[0] * n for _ in range(n)]

        # Base case: the last row of dp is same as the last row of triangle
        for i in range(n):
            dp[n - 1][i] = tri[n - 1][i]

        # Start filling dp table from bottom to top
        for cur_row in range(n - 2, -1, -1):   # from second-last row to top
            for i in range(cur_row, -1, -1):   # each element in current row

                # Two choices:
                # 1. Move straight down (dp[cur_row+1][i])
                # 2. Move diagonally down-right (dp[cur_row+1][i+1])
                first = dp[cur_row + 1][i] + tri[cur_row][i]
                second = dp[cur_row + 1][i + 1] + tri[cur_row][i]

                # Store minimum of both choices
                dp[cur_row][i] = min(first, second)

        # Final answer: minimum path sum from top element (0,0)
        return dp[0][0]
