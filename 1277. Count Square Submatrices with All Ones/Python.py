# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def f(self, i, j, mat, m, n, dp):
        if i >= m or j >= n:
            return 0

        if mat[i][j] == 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        right = self.f(i, j + 1, mat, m, n, dp)
        diag = self.f(i + 1, j + 1, mat, m, n, dp)
        down = self.f(i + 1, j, mat, m, n, dp)

        dp[i][j] = 1 + min(right, diag, down)
        return dp[i][j]

    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]


        ans = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == 1:
                    right = dp[i][j + 1]
                    diag = dp[i + 1][j + 1]
                    down = dp[i + 1][j]

                    dp[i][j] = 1 + min(right, diag, down)
                    ans += dp[i][j]

        return ans