# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array in ascending order

        ans = 1      # At least one subarray is needed

        mini = nums[0]  # Track the minimum element in the current subarray

        # Iterate through the sorted numbers
        for i in nums:
            # If the current element is too far from the minimum of the current group,
            # start a new subarray
            if i - mini > k:
                ans += 1      # Increase the number of required subarrays
                mini = i      # Reset the minimum for the new subarray

        return ans  # Return the total number of subarrays needed
