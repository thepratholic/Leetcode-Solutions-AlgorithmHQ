# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float("-inf")

        for i in range(n - 1):
            ans = max(ans, abs(nums[i] - nums[i + 1])) # calculate the absolute difference between adjacent elements

        ans = max(ans, abs(nums[0] - nums[-1])) # calculate the absolute difference btween first and last elements for circular array

        return ans  # return the maximum abs answer