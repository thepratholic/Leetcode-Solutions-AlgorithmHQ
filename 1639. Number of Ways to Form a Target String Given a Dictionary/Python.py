# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import Counter
from typing import List

M = 10 ** 9 + 7  # Modulo to prevent overflow

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m = len(target)  # Length of the target string
        n = len(words[0])  # Length of each word in words

        # Step 1: Precompute character frequencies at each position in the words
        chars = [Counter() for _ in range(n)]
        for w in words:
            for i in range(n):
                chars[i][w[i]] += 1  # Count occurrences of each character at position i

        # Step 2: Initialize the DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: If we've formed the entire target, there is 1 way (do nothing)
        for i in range(n + 1):
            dp[m][i] = 1

        # Step 3: Fill the DP table in reverse order
        for i in range(m - 1, -1, -1):  # Iterate over the target string
            for j in range(n - 1, -1, -1):  # Iterate over positions in the words
                # Option 1: Skip the current position in `words`
                dp[i][j] = dp[i][j + 1]
                
                # Option 2: Use the current position if it matches the target character
                if chars[j][target[i]] > 0:  # Check if target[i] exists in chars[j]
                    dp[i][j] += chars[j][target[i]] * dp[i + 1][j + 1]
                
                # Apply modulo to prevent overflow
                dp[i][j] %= M

        # The result is the number of ways to form the entire target from position 0
        return dp[0][0]
