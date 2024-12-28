# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)  # Length of the input array
        # Initialize arrays to track the maximum sums and their starting indices
        starts = [(float('-inf'), -1)] * n  # Tracks max sum of subarray starting at or after each index
        ends = [(float('-inf'), -1)] * n  # Tracks max sum of subarray ending at or before each index
        s = 0  # Sliding window sum for subarrays of size k

        # First pass: Compute subarray sums for both `starts` and `ends`
        for i in range(n):
            s += nums[i]  # Add the current number to the sliding window sum
            if i >= k:  # Remove the number that's sliding out of the window
                s -= nums[i - k]
            if i >= k - 1:  # Ensure the window size is exactly k
                # Update `starts` for the subarray starting at i - k + 1
                starts[i - k + 1] = (s, i - k + 1)
                # Update `ends` for the subarray ending at i
                ends[i] = (s, i - k + 1)

        # Propagate maximum sums to ensure global maximum is maintained
        # For `ends`, propagate left to right
        for i in range(1, n):
            ends[i] = max(ends[i], ends[i - 1])

        # For `starts`, propagate right to left
        for i in range(n - 2, -1, -1):
            starts[i] = max(starts[i], starts[i + 1])

        # Initialize the result to track the best combination of subarrays
        res = (float('-inf'), -n, -n, -n)  # (max_sum, left_start, middle_start, right_start)
        s = 0  # Reset sliding window sum for the middle subarray

        # Iterate to find the best middle subarray and compute the total sum
        for i in range(n):
            s += nums[i]  # Add current number to the sliding window sum
            if i >= k:  # Remove the number that's sliding out of the window
                s -= nums[i - k]
            # Check if the current subarray can serve as the middle subarray
            if k - 1 < i < n - 1:  # Ensure there is space for left and right subarrays
                # Calculate the total sum of the three subarrays
                currs = ends[i - k][0] + s + starts[i + 1][0]
                # Update the result if this combination has a larger sum
                res = max(res, (currs, ends[i - k][1], i - k + 1, starts[i + 1][1]))

        # Return the starting indices of the three subarrays in sorted order
        return [res[1], res[2], res[3]]
