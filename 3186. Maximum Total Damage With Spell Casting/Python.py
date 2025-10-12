# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from bisect import bisect_right
from typing import Counter, List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        n = len(power)
        freq = Counter(power)  # Count the frequency of each power value

        if n == 1:
            return power[0]  # If only one element, the answer is itself

        power.sort()  # Sort the powers for easier "next non-adjacent" selection

        # Recursive function to compute max damage starting from index idx
        def f(idx):
            if idx >= n:
                return 0  # Base case: reached beyond array

            if dp[idx] != -1:
                return dp[idx]  # Return cached result

            # Option 1: Do not take current power[idx]
            notTake = f(idx + 1)

            # Option 2: Take current power[idx]
            nxt = power[idx] + 2  # We must skip all numbers equal to power[idx]+1
            next_idx = bisect_right(power, nxt - 1)  # Find first index where power >= nxt
            take = power[idx] * freq[power[idx]] + f(next_idx)  # Total damage if we take all freq of current

            # Memoize the maximum of taking vs not taking
            dp[idx] = max(take, notTake)
            return dp[idx]

        dp = [-1] * n  # Initialize DP array for memoization
        return f(0)  # Start recursion from index 0
