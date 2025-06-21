# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        # Count the frequency of each letter and sort them in increasing order
        freq = sorted(Counter(word).values())

        ans = float("inf")  # Initialize minimum deletions to infinity
        n = len(freq)

        # Try using each frequency as the base frequency
        for i in range(n):
            base = freq[i]  # The base frequency to keep

            ops = 0  # Number of deletions needed for this base

            for f in freq:
                if f < base:
                    # If frequency is less than base, delete entire letters
                    ops += f
                elif f > base + k:
                    # If frequency is greater than base + k, reduce it to base + k
                    ops += f - (base + k)
                # If within [base, base + k], no deletion needed

            # Update the minimum deletions across all choices
            ans = min(ans, ops)

        return ans