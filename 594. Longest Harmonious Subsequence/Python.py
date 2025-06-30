# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Sort the array to make it easier to find consecutive numbers
        nums.sort()
        
        ans = 0  # Store the length of the longest harmonious subsequence
        l, r = 0, 1  # Two pointers: l is left boundary, r is right boundary

        while r < n:
            # If the current window has a difference of exactly 1
            if nums[r] - nums[l] == 1:
                ans = max(ans, r - l + 1)

            # If difference is more than 1, move left pointer forward
            while nums[r] - nums[l] > 1:
                l += 1

            # Move right pointer forward in each iteration
            r += 1

        return ans
