# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict

class Solution:
    def maxDifference(self, s: str) -> int:
        n = len(s)

        mpp = defaultdict(int)  # Dictionary to store frequency of each character

        # Count the frequency of each character in the string
        for i in s:
            mpp[i] += 1

        max_even = float('inf')  # Initialize to large value for finding minimum even frequency
        max_odd = 0              # Initialize to zero for finding maximum odd frequency

        # Iterate over all character frequencies
        for v in mpp.values():
            if v % 2 == 1:  # If frequency is odd
                max_odd = max(max_odd, v)
            else:  # If frequency is even
                max_even = min(max_even, v)

        # Return the difference between largest odd freq and smallest even freq
        return max_odd - max_even
