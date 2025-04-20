class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # Define the modulo constant
        MOD = 10**9 + 7

        def f(x, n):
            """
            Fast exponentiation function to compute (x^n) % MOD.
            """
            res, mul = 1, x  # Initialize result to 1 and current multiplier as x
            
            # Process the exponent using binary exponentiation
            while n > 0:
                # If the current bit (least significant bit) of n is 1, multiply result by current multiplier
                if n % 2 == 1:
                    res = (res * mul) % MOD
                # Square the multiplier for the next bit
                mul = (mul * mul) % MOD
                # Right shift the exponent (divide by 2)
                n //= 2
            
            return res

        # Explanation of the final return:
        # According to the problem, a "good number" can be formed using:
        # - 5 in each odd-indexed position (1-based) 
        # - 4 in each even-indexed position (1-based)
        # Therefore, for a number of length n:
        #   - The count of odd positions = ceil(n/2) = (n + 1) // 2.
        #   - The count of even positions = n // 2.
        # The total number of good numbers is:
        #   5^( (n + 1) // 2 ) * 4^( n // 2 ) modulo MOD.
        return f(5, (n + 1) // 2) * f(4, n // 2) % MOD
