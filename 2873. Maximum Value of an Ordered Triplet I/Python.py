# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)  # Get the size of the array

        maxi = float("-inf")  # Initialize the maximum value with negative infinity

        # Iterate through all possible triplets (i, j, k) where i < j < k
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    # Calculate the expression (nums[i] - nums[j]) * nums[k]
                    maxi = max(maxi, (nums[i] - nums[j]) * nums[k])

        # Return the maximum value found, ensuring that the result is non-negative
        return maxi if maxi > 0 else 0
