# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == len(set(nums)): # if the given list is already have distinct elements
            return 0
        cnt = 0 # to count the number of operations to make array elements distinct

        while nums: # we always check if nums is there, then remove first three elements from it
            nums = nums[3:]
            cnt += 1 # incrementing the operation everytime

            if len(nums) == len(set(nums)): # if the list have distinct elements after any operation, then we return cnt
                return cnt

        return cnt