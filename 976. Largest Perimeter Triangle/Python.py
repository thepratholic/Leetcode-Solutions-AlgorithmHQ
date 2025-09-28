# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sort the array in descending order (largest to smallest)
        # because the largest perimeter will come from the biggest sides
        nums.sort(reverse = True)
        n = len(nums)

        # Iterate through each triplet of numbers (a, b, c)
        # starting from the largest values
        for i in range(n - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]

            # Check the triangle inequality condition:
            # sum of smaller two sides (b + c) must be greater than largest side (a)
            if b + c > a:
                # If valid triangle, return its perimeter
                return a + b + c

        # If no valid triangle is found, return 0
        return 0
