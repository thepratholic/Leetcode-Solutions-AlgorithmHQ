# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        
        t = 1   # number of operations (we will keep trying with increasing t)

        while True:
            # After t operations, we subtract (t * num2) from num1
            val = num1 - (t * num2)

            # If remaining value becomes less than t, 
            # it's impossible because we need at least `t` numbers to represent val
            if val < t:
                return -1

            # Count minimum bits required to represent val in binary
            # (this is same as counting number of 1s in its binary representation)
            min_bits = val.bit_count()

            # If val can be represented using at most t numbers (min_bits ≤ t),
            # then we found our answer
            if min_bits <= t:
                return t

            # Otherwise, try with next larger t
            t += 1