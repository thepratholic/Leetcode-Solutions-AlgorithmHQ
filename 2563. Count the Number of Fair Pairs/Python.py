# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()  # Sort the array to apply two-pointer approach

        # Count pairs where sum <= upper
        left, right = 0, n - 1
        cnt_within_upper = 0

        while left < right:
            if nums[left] + nums[right] <= upper:
                # All values from left to right-1 with nums[right] will also be valid
                cnt_within_upper += (right - left)
                left += 1
            else:
                right -= 1

        # Count pairs where sum < lower
        left, right = 0, n - 1
        cnt_below_lower = 0

        while left < right:
            if nums[left] + nums[right] < lower:
                # All values from left to right-1 with nums[right] will be invalid (too small)
                cnt_below_lower += (right - left)
                left += 1
            else:
                right -= 1

        # Final result = pairs within [lower, upper] range
        return cnt_within_upper - cnt_below_lower
