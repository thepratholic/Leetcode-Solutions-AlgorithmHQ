# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        OR = 0  # Step 1: Find OR of all numbers
        for num in nums:
            OR |= num

        # Step 2: Each bit in OR contributes in 2^(n-1) subsets
        return OR * (1 << (n - 1))
