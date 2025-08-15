# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 0 and n % 4 == 0: # while n is divisible by 4 and is greater than 0, till then divide it by 4
            n //= 4

        return n == 1 # return true if n is 1 else false