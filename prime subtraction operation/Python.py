from math import sqrt
from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def isPrime(n):
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    return False
            return True

        prev = 0
        for n in nums:
            upperBound = n - prev # it is non-inclusive

            largest_p = 0
            for i in reversed(range(2, upperBound)):
                if isPrime(i):
                    largest_p = i
                    break

            if n - largest_p <= prev:
                return False
            prev = n - largest_p

        return True


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/