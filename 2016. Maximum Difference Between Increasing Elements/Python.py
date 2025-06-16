# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = float("-inf")  # Initialize answer as negative infinity
        n = len(nums)

        # Try all pairs (i, j) with j >= i
        for i in range(n - 1):
            for j in range(i, n):
                # Check if nums[j] is larger than nums[i]
                if nums[j] > nums[i]:
                    ans = max(ans, nums[j] - nums[i])  # Update maximum difference

        # If no valid pair found, return -1
        return ans if ans != float("-inf") else -1
