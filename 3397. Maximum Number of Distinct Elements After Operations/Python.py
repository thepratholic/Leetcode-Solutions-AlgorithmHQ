# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import Counter
from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Base case: if we can't move any element, 
        # simply count distinct numbers in nums
        if k == 0:
            return len(set(nums))

        # Step 1: Sort to handle elements in increasing order
        nums.sort()
        
        # Step 2: Initialize result
        count = 1

        # 'prev' stores the last used distinct value
        # We start with nums[0] - k because we can reduce nums[0] by up to k
        prev = nums[0] - k

        # Step 3: Traverse the rest of the array
        for i in range(1, n):

            # We want the current distinct number to be at least 1 greater than 'prev'
            # But we can only move nums[i] in range [nums[i] - k, nums[i] + k]
            # So, we take the maximum possible starting point that keeps array distinct
            cur_mini = max(prev + 1, nums[i] - k)

            # If this adjusted number is still within allowed range [nums[i] - k, nums[i] + k],
            # we can use it as a distinct element
            if cur_mini <= nums[i] + k:
                count += 1      # Found another distinct value
                prev = cur_mini # Update last used distinct value

            else:
                # If even after adjusting, we can't make it distinct,
                # we move 'prev' to the upper bound for next elements
                prev = nums[i] + k

        # Step 4: Return total distinct count
        return count
