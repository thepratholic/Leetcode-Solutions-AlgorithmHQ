# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        # Recursive function f(i, j) will return the minimum triangulation score 
        # of the polygon formed by vertices from index i to j.
        def f(i, j):
            # Base case: If fewer than 3 vertices, no triangle can be formed
            if j - i + 1 < 3:
                return 0

            # If already computed, return memoized result
            if dp[i][j] != -1:
                return dp[i][j]

            ans = float("inf")  # Start with very large value

            # Try all possible partitions: choose a vertex k between (i, j)
            # Form triangle (i, k, j) and recursively compute for left & right sub-polygons
            for k in range(i + 1, j):
                # Triangle score for vertices i, j, k
                t = values[i] * values[j] * values[k]

                # Total score = left polygon + triangle + right polygon
                wt = f(i, k) + t + f(k, j)

                # Take the minimum score
                ans = min(ans, wt)

            # Store in dp table and return
            dp[i][j] = ans
            return dp[i][j]

        # Memoization table initialized with -1
        dp = [[-1] * n for _ in range(n)]
        
        # Solve for the full polygon (0 ... n-1)
        return f(0, n - 1)
