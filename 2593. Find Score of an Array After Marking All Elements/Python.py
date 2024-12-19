# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/thepratholic/

from sortedcontainers import SortedList
from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        vals = SortedList()  # Initialize the sorted list

        # Add all elements with their indices into the sorted list
        for i in range(n):
            vals.add((nums[i], i))

        res = 0  # Initialize the score

        # Process the elements in sorted order
        while vals:
            v, pos = vals.pop(0)  # Get the smallest value and its index
            res += v  # Add its value to the result

            # Remove neighbors if they exist in the sorted list
            for x in [pos - 1, pos + 1]:
                if 0 <= x < n and (nums[x], x) in vals:
                    vals.remove((nums[x], x))

        return res
