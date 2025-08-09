class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 # Performing n & (n - 1) will result in 0 only for powers of two.