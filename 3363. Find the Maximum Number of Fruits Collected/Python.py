# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    # --------------------
    # Child 1: Picks fruits from the main diagonal (top-left to bottom-right)
    # --------------------
    def child1Fruits(self, fruits):
        n = len(fruits)
        ans = 0
        for i in range(n):
            ans += fruits[i][i]   # Add fruit from the diagonal
            fruits[i][i] = 0      # Mark as collected so no one else picks it
        return ans

    # --------------------
    # Child 2: Starts from top-right corner and moves down
    # Allowed moves: bottom-left, bottom-down, bottom-right
    # --------------------
    def child2Fruits(self, i, j, fruits, dp):
        n = len(fruits)
        
        # Out-of-bound check
        if i >= n or j < 0 or j >= n:
            return 0
        
        # Reached bottom-right corner (stop collecting)
        if i == n - 1 and j == n - 1:
            return 0
        
        # Invalid positions: same cell as other child (diagonal) or crossed path
        if i == j or i > j:
            return 0
        
        # Return precomputed result
        if dp[i][j] != -1:
            return dp[i][j]
        
        # Move bottom-left
        bottomLeft = fruits[i][j] + self.child2Fruits(i + 1, j - 1, fruits, dp)
        # Move straight down
        bottomDown = fruits[i][j] + self.child2Fruits(i + 1, j, fruits, dp)
        # Move bottom-right
        bottomRight = fruits[i][j] + self.child2Fruits(i + 1, j + 1, fruits, dp)
        
        # Store best result for current position
        dp[i][j] = max(bottomLeft, bottomDown, bottomRight)
        return dp[i][j]

    # --------------------
    # Child 3: Starts from bottom-left corner and moves right/up
    # Allowed moves: up-right, right, bottom-right
    # --------------------
    def child3Fruits(self, i, j, fruits, dp):
        n = len(fruits)
        
        # Out-of-bound check
        if i < 0 or j >= n or i >= n:
            return 0
        
        # Reached bottom-right corner (stop collecting)
        if i == n - 1 and j == n - 1:
            return 0
        
        # Invalid positions: same cell as other child (diagonal) or crossed path
        if i == j or i < j:
            return 0
        
        # Return precomputed result
        if dp[i][j] != -1:
            return dp[i][j]
        
        # Move up-right
        upRight = fruits[i][j] + self.child3Fruits(i - 1, j + 1, fruits, dp)
        # Move straight right
        right = fruits[i][j] + self.child3Fruits(i, j + 1, fruits, dp)
        # Move bottom-right
        bottomRight = fruits[i][j] + self.child3Fruits(i + 1, j + 1, fruits, dp)
        
        # Store best result for current position
        dp[i][j] = max(upRight, right, bottomRight)
        return dp[i][j]

    # --------------------
    # Main function to collect maximum fruits by all three children
    # --------------------
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        # 1️⃣ Child 1 collects diagonal fruits
        c1 = self.child1Fruits(fruits)

        # 2️⃣ Child 2 collects from top-right to bottom
        dp2 = [[-1] * n for _ in range(n)]
        c2 = self.child2Fruits(0, n - 1, fruits, dp2)

        # 3️⃣ Child 3 collects from bottom-left to right
        dp3 = [[-1] * n for _ in range(n)]
        c3 = self.child3Fruits(n - 1, 0, fruits, dp3)

        # Total fruits collected
        return c1 + c2 + c3
