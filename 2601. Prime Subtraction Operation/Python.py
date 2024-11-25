# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from math import sqrt
from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Helper function to check if a number is prime
        def isPrime(n):
            for f in range(2, int(sqrt(n)) + 1):  # Check divisibility from 2 to sqrt(n)
                if n % f == 0:  # If divisible, n is not prime
                    return False
            return True  # n is prime if no divisors found

        prev = 0  # Initialize previous value to 0 to track the last modified element in the array
        for n in nums:
            # Calculate the upper bound for prime subtraction
            upperBound = n - prev  # This is the maximum value we can subtract from n (non-inclusive)

            largest_p = 0

            for i in reversed(range(2, upperBound)):
                if isPrime(i):
                    largest_p = i  # Found the largest prime
                    break

            # If the difference between n and the largest prime is not greater than the previous value,
            # it means the operation is not possible
            if n - largest_p <= prev:
                return False
            prev = n - largest_p  # Update prev for the next iteration with the new value after subtraction

        return True
