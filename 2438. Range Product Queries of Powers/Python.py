# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7  # Problem constraint: large numbers, so use modulo
        powers = []

        # -----------------------------------------------------
        # Step 1: Extract the powers of two that sum to 'n'
        # Each bit set in 'n' corresponds to a power of two.
        # -----------------------------------------------------
        bit = 0
        while n > 0:
            if n & 1:  # If the current bit is set
                powers.append(1 << bit)  # Add corresponding 2^bit
            n >>= 1    # Shift right to process next bit
            bit += 1

        # -----------------------------------------------------
        # Step 2: Precompute prefix products of 'powers'
        # prod[i] = product of powers[0] to powers[i] (modulo mod)
        # -----------------------------------------------------
        prod = [-1] * len(powers)
        prod[0] = powers[0] % mod
        for i in range(1, len(powers)):
            prod[i] = (prod[i - 1] * powers[i]) % mod

        # -----------------------------------------------------
        # Step 3: Answer each query efficiently using prefix products
        # Query [l, r] means: multiply powers[l] * ... * powers[r]
        # If l > 0, divide by prod[l - 1] (modular inverse)
        # -----------------------------------------------------
        answer = []
        for l, r in queries:
            if l == 0:
                answer.append(prod[r])  # Direct prefix product
            else:
                # Modular inverse: Fermat's Little Theorem
                inv = pow(prod[l - 1], mod - 2, mod)
                answer.append((prod[r] * inv) % mod)

        return answer
