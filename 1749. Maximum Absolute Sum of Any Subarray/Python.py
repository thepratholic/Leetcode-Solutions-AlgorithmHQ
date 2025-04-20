# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/thepratholic/

from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maximum_sum = float('-inf')  # To store the maximum subarray sum
        n = len(nums)  # Length of the array

        # Finding the Maximum Subarray Sum (Kadane's Algorithm)
        current = 0
        for i in range(n):
            current += nums[i]  # Add current element to the subarray sum
            maximum_sum = max(maximum_sum, current)  # Update the max sum
            if current < 0:
                current = 0  # Reset the sum if it becomes negative

        # Finding the Minimum Subarray Sum (Kadane’s Algorithm for Min)
        minimum_sum = float('inf')  # To store the minimum subarray sum
        current = 0
        for i in range(n):
            current += nums[i]  # Add current element to the subarray sum
            minimum_sum = min(minimum_sum, current)  # Update the min sum
            if current > 0:
                current = 0  # Reset the sum if it becomes positive

        # Return the maximum absolute value of the two
        return max(maximum_sum, abs(minimum_sum))
