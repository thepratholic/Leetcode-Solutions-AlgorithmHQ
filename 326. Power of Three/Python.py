# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: # if the number is zero or negative, then it is not possible to represent as the power of 3
            return False

        while n % 3 == 0: # while n is divisible by 3, till then divide it by 3
            n //= 3

        return n == 1 # return true if n is 1 else false