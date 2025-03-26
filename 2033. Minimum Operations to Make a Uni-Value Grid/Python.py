# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        # Step 1: Check if transformation is possible
        for row in grid:
            for e in row:
                # If remainder of any element with x is different, transformation is impossible
                if e % x != grid[0][0] % x:
                    return -1

        # Step 2: Flatten the 2D grid into a 1D list and sort it
        nums = sorted([ele for row in grid for ele in row])

        # Step 3: Compute minimum operations using the median
        prefix = 0  # Prefix sum for left part
        total = sum(nums)  # Total sum of all elements
        ans = float("inf")  # Initialize minimum operations as infinity

        # Traverse through sorted numbers to find the optimal target
        for i in range(len(nums)):
            cost_left = nums[i] * i - prefix  # Cost to convert left part to nums[i]
            cost_right = total - prefix - (nums[i] * (len(nums) - i))  # Cost for right part
            ops = (cost_left + cost_right) // x  # Compute operations by dividing by x
            ans = min(ans, ops)  # Update minimum operations found
            prefix += nums[i]  # Update prefix sum
        
        return ans
