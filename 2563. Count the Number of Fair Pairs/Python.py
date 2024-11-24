# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def lower_bound(self, nums, value):
        left, right = 0, len(nums) - 1
        res = 0

        # Use two-pointer technique to count pairs with sum < value.
        while left < right:
            sum = nums[left] + nums[right]
            if sum < value:
                # All pairs between `left` and `right` have a sum < value.
                res += (right - left)
                left += 1
            else:
                right -= 1
        return res

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        # Count pairs in the range [lower, upper] using `lower_bound`.
        # `upper + 1` ensures pairs with sum <= upper are included.
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)
