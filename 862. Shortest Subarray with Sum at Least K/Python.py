# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float("inf")  # Initialize the result with infinity, which will represent the minimum length
        q = deque()  # A deque to store pairs of (current prefix sum, index)
        curSum = 0  # Initialize the current prefix sum

        # Iterate through the array
        for r in range(len(nums)):
            curSum += nums[r]  # Update the current prefix sum by adding the current element
            
            # Check if the current prefix sum is already >= k, and update the result
            if curSum >= k:
                res = min(res, r + 1)

            # Check if the difference between current sum and earlier prefix sums is >= k
            while q and curSum - q[0][0] >= k:
                pre, end = q.popleft()  # Remove the front element of the deque (oldest prefix sum)
                res = min(res, r - end)  # Update the result with the shortest subarray length

            # Maintain a monotonically increasing deque
            while q and q[-1][0] > curSum:
                q.pop()  # Remove elements from the back of the deque if they are greater than the current prefix sum
            
            # Add the current prefix sum and its index to the deque
            q.append((curSum, r))

        # If no valid subarray is found, return -1; otherwise, return the result
        return -1 if res == float("inf") else res
