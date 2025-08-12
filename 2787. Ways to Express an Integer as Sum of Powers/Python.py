# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

mod = 10 ** 9 + 7  # Modulo constant to prevent integer overflow in large results

class Solution:
    # Recursive helper function to count ways
    def f(self, n, cur_num, x, dp):
        # Base case: If we have exactly reached sum 0, it means we found a valid way
        if n == 0:
            return 1

        # If sum becomes negative, this path is invalid
        if n < 0:
            return 0

        # Calculate current number raised to the power x
        currentPowerVal = cur_num ** x
        
        # If current power is greater than remaining sum, we can't proceed
        if currentPowerVal > n:
            return 0
        
        # Check memoization table to avoid recomputation
        if dp[n][cur_num] != -1:
            return dp[n][cur_num]
        
        # Choice 1: Pick the current number (reduce n by current power, move to next number)
        pick = self.f(n - currentPowerVal, cur_num + 1, x, dp)
        
        # Choice 2: Skip the current number and move to next
        notPick = self.f(n, cur_num + 1, x, dp)

        # Store the result in dp table after applying modulo
        dp[n][cur_num] = (notPick + pick) % mod
        
        return dp[n][cur_num]

    def numberOfWays(self, n: int, x: int) -> int:
        # DP table: dp[remaining_sum][current_number]
        # Initialize with -1 meaning "not computed yet"
        dp = [[-1] * 301 for _ in range(301)]
        
        # Start recursion with sum = n, current number = 1
        return self.f(n, 1, x, dp)
