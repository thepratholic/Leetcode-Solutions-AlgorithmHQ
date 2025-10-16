# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from collections import defaultdict
from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # Dictionary to store frequency of each remainder mod 'value'
        mpp = defaultdict(int)

        # Step 1: Calculate normalized remainder frequencies
        for num in nums:
            # Normalize remainder to be always positive
            # (for negative nums, Python's % gives negative remainder)
            r = ((num % value) + value) % value
            mpp[r] += 1

        # Step 2: Try to form smallest missing number (mex)
        mex = 0

        # While there exists an available number in the same remainder class,
        # we can represent current mex, so we consume one occurrence.
        while mpp[(mex % value)] > 0:
            mpp[(mex % value)] -= 1
            mex += 1

        # Step 3: Return the first missing number that couldn't be formed
        return mex
