# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)

        # If only one number, that itself is the triangular sum
        if n == 1:
            return nums[0]

        # Function to generate the next row by summing adjacent elements
        def f(arr):
            # New array will be one element shorter
            newNums = [-1] * (len(arr) - 1)

            # Each element is sum of two adjacent numbers modulo 10
            for i in range(len(arr) - 1):
                newNums[i] = (arr[i] + arr[i + 1]) % 10

            return newNums

        # Start by reducing the given array once
        newArr = f(nums)

        # Keep reducing until only one element remains
        while True:
            if len(newArr) == 1:
                # Final element is the triangular sum
                return newArr[0]
            else:
                # Reduce again
                newArr = f(newArr)
