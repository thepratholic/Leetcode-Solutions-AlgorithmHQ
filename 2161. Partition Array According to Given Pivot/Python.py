# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/thepratholic/

from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        n = len(nums)  # Length of the input list
        less, more = [], []  # Lists to store numbers less and greater than pivot

        # First pass: Separate numbers less than and greater than pivot
        for i in range(n):
            if nums[i] < pivot:
                less.append(nums[i])  # Store numbers less than pivot

            if nums[i] > pivot:
                more.append(nums[i])  # Store numbers greater than pivot

        # Second pass: Collect all pivot elements (preserving order)
        for i in range(n):
            if nums[i] == pivot:
                less.append(nums[i])  # Append pivot elements after smaller ones

        # Combine results
        res = []
        res.extend(less)  # Add smaller + pivot elements
        res.extend(more)  # Add larger elements
        return res
