# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/thepratholic/

from typing import List


class Solution:
    def shiftZeros(self, nums):
        # Initialize index 'j' to track the first zero position
        j = -1  
        
        # Find the first zero in the array
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break  # Stop at the first occurrence of zero
        
        # If no zeros are found, return the array as is
        if j == -1: 
            return nums

        # Move non-zero elements forward and push zeros to the end
        for k in range(j + 1, len(nums)):
            if nums[k] != 0:
                nums[j], nums[k] = nums[k], nums[j]  # Swap zero with non-zero element
                j += 1  # Move 'j' pointer to the next zero position

        return nums

    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Iterate through the array and apply the doubling rule
        for i in range(n-1):
            if nums[i] == nums[i+1]:  # If two adjacent numbers are equal
                nums[i] *= 2  # Double the first number
                nums[i+1] = 0  # Set the second number to zero

        # Shift all zeros to the end while maintaining order
        return self.shiftZeros(nums)
