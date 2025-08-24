# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/thepratholic/

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)                 # Length of the input array
        f = False                     # Flag to check if at least one zero exists
        zeros = 0                     # Count of zeros in the current sliding window

        l, r = 0, 0                   # Left and right pointers for sliding window
        ans = float('-inf')           # Stores the maximum length result

        while r < n:                  # Iterate with right pointer

            if nums[r] == 0:          # If current element is 0
                zeros += 1            # Increase zero count
                f = True              # Mark that we have seen at least one zero

            # Shrink the window if we have more than 1 zero
            while zeros > 1 and l <= r:
                if nums[l] == 0:      # If leftmost element is 0
                    zeros -= 1        # Reduce zero count
                l += 1                # Move left pointer forward

            # Case 1: If we have at least one zero in the array
            if f:
                # (r - l + 1) → length of current window
                # subtract zeros (we only allow max one zero to delete)
                ans = max(ans, (r - l + 1) - zeros)

            # Case 2: If no zero exists in the array (all 1s case)
            else:
                # Must delete one element, so subtract 1
                ans = max(ans, (r - l + 1) - 1)

            r += 1                    # Expand window to the right

        return ans                    # Return the maximum length found