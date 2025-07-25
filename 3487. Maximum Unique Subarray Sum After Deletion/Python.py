# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)

        s = set()

        for i in range(n):
            if nums[i] > 0:
                s.add(nums[i]) # add only positive numbers

        if len(s) == 0:
            return max(nums) # if every number in nums is < 0, then return the maximum one

        else:
            return sum(s) # otherwise return the sum of the positive numbers