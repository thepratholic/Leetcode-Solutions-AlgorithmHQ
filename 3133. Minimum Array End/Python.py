class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        n -= 1
        mask = 1

        while n > 0:
            # If the corresponding bit in x is 0
            if (mask & x) == 0:
                # we set bit in the result
                res |= (n & 1) * mask
                # shifting n by 1 to process next bit
                n >>= 1
            mask <<= 1

        return res


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/
