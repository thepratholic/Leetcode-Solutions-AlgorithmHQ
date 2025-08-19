# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)  # Length of the input array

        # This array will store, for each index i, 
        # the number of consecutive zeros ending at position i
        zeros = [0] * n  

        # If the very first element is zero, 
        # then there is exactly 1 zero-filled subarray ending at index 0
        if nums[0] == 0:
            zeros[0] = 1  

        # Fill the zeros[] array
        for i in range(1, n):
            if nums[i] == 0:
                # If nums[i] is 0, then the number of zero-subarrays ending at i 
                # = 1 (the element itself) + number of zero-subarrays ending at i-1
                zeros[i] = 1 + zeros[i - 1]
            else:
                # If nums[i] is not 0, no zero-subarray can end here
                zeros[i] = 0  

        ans = 0  # Will hold the total count of zero-filled subarrays

        # Sum up all values in zeros[], 
        # because each zeros[i] tells how many zero-subarrays end at i
        for i in range(n):
            ans += zeros[i]

        return ans  # Final answer
