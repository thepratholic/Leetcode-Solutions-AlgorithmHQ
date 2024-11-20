from typing import List


class Solution:
    def lower_bound(self, nums, value):
        left, right = 0, len(nums) - 1
        res = 0
        n = len(nums)
        while left < right:
            sum = nums[left] + nums[right]
            if sum < value:
                res += (right - left)
                left += 1
            else:
                right -= 1
        return res

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/