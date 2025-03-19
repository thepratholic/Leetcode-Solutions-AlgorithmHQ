# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)  # Get length of nums
        cnt = 0  # Operation count

        # Iterate from index 2 to n-1
        for i in range(2, n):
            if nums[i - 2] == 0:  # If we find a '0' at position i-2
                cnt += 1  # Increment operation count

                # Flip the triplet nums[i-2], nums[i-1], nums[i]
                nums[i - 2] ^= 1  
                nums[i - 1] ^= 1  
                nums[i] ^= 1  

        # Check if all elements are 1
        if sum(nums) == len(nums):
            return cnt  # Return number of operations

        return -1  # If not possible, return -1
