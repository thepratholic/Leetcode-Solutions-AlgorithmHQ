# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)

        # Variable to store the maximum energy sum found so far
        maxi = float('-inf')

        # dp[i] = maximum energy sum starting from index i
        # We take n+1 to safely handle index i+k when i is near the end
        dp = [0] * (n + 1)

        # Base condition: dp[n] = 0 (no energy beyond last element)
        dp[n] = 0

        # Traverse the energy array in reverse order
        # Because each state dp[i] depends on dp[i + k]
        for i in range(n - 1, -1, -1):

            # If jumping k steps ahead is within the array bounds
            if i + k < n:
                dp[i] = energy[i] + dp[i + k]
            else:
                # If out of bounds, only take the current energy value
                dp[i] = energy[i]

            # Update the global maximum
            maxi = max(maxi, dp[i])

        # The overall maximum energy path
        return maxi
