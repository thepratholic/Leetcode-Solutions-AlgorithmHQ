# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict
from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Total pairs possible in an array of size n: C(n,2) = n * (n - 1) // 2
        total_pairs = n * (n - 1) // 2
        
        diff_count = defaultdict(int)  # Dictionary to store frequency of (nums[i] - i)
        good_pairs = 0  # Counter for good pairs

        # Iterate through the array
        for i in range(n):
            diff = nums[i] - i  # Compute the difference (nums[i] - i)

            # If this difference has appeared before, it means we found good pairs
            good_pairs += diff_count[diff]
            
            # Increment the count of this difference for future comparisons
            diff_count[diff] += 1

        # Bad pairs = total pairs - good pairs
        return total_pairs - good_pairs
