from collections import defaultdict
from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l = 0  # Left pointer of the sliding window
        res = 0  # To store final result: total number of good subarrays
        pairs = 0  # To keep track of number of "equal pairs" in current window
        freq = defaultdict(int)  # Frequency map to store count of elements in current window

        # Right pointer of the window moves from left to right
        for r in range(len(nums)):
            # Before adding nums[r] to the window, we already have freq[nums[r]] elements
            # Adding it will make `freq[nums[r]]` new pairs with the same value
            pairs += freq[nums[r]]
            freq[nums[r]] += 1

            # Now shrink the window from the left while we have enough pairs (>= k)
            while pairs >= k:
                # All subarrays starting from l to len(nums)-1 and ending at r are valid
                res += len(nums) - r

                # We remove nums[l] from the window and update pair count
                freq[nums[l]] -= 1
                # Removing one occurrence reduces the pair count by `freq[nums[l]]`
                pairs -= freq[nums[l]]
                l += 1

        return res
