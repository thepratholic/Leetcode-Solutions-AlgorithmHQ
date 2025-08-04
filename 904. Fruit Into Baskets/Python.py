# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('-inf')  # To keep track of the maximum number of fruits collected
        mpp = defaultdict(int)  # Dictionary to count the number of fruits of each type in the current window

        l, r = 0, 0  # Left and right pointers for the sliding window

        while r < n:
            mpp[nums[r]] += 1  # Add the current fruit at r to the basket (increase count)

            # If we have more than 2 types of fruits, shrink the window from the left
            if len(mpp) > 2:
                while mpp[nums[l]] > 0:
                    mpp[nums[l]] -= 1  # Remove one fruit from the left
                    if mpp[nums[l]] == 0:  # If no fruits of this type are left, remove the type from the map
                        del mpp[nums[l]]
                        break
                    l += 1
                l += 1  # Move the left pointer ahead after removing excess type

            # Update maximum size of valid window
            ans = max(ans, r - l + 1)
            r += 1  # Move right pointer ahead

        return ans
