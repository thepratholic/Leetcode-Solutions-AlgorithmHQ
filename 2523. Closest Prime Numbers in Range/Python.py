# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/thepratholic/


from typing import List

class Solution:
    def primeTillN(self, n):
        """ Returns a list of prime numbers up to 'n' using the Sieve of Eratosthenes. """
        if n < 2:
            return []

        isprime = [1] * (n + 1)  # Assume all numbers are prime
        isprime[0] = isprime[1] = 0  # 0 and 1 are not prime
        ans = []  # Store prime numbers

        for i in range(2, n + 1):
            if isprime[i]:  # If 'i' is prime
                ans.append(i)  # Add to list
                for val in range(i * i, n + 1, i):  # Mark multiples as non-prime
                    isprime[val] = 0

        return ans

    def closestPrimes(self, left: int, right: int) -> List[int]:
        """ Returns the closest pair of prime numbers in the range [left, right]. """
        primes = self.primeTillN(right)  # Get primes up to 'right'
        ans = [-1, -1]  # Default answer
        tmp = [p for p in primes if p >= left]  # Filter primes in range [left, right]

        # If less than 2 primes exist, return [-1, -1]
        if len(tmp) < 2:
            return [-1, -1]

        # Find the closest prime pair
        mini = float('inf')
        for j in range(len(tmp) - 1):  # Traverse normally from left to right
            if tmp[j + 1] - tmp[j] < mini:
                mini = tmp[j + 1] - tmp[j]
                ans[0], ans[1] = tmp[j], tmp[j + 1]

        return ans  # Return the closest prime pair
