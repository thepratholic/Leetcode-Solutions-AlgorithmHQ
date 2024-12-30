# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    # Recursive function to count ways to assign symbols (+ or -) to make the sum equal to the target
    def count(self, nums, i, n, curr, target):

        # Base case: When all elements are considered
        if i >= n:
            # Check if the current cumulative sum is half of the target (since we're dealing with sums split into + and -)
            if 2 * curr == target:
                return 1  # Valid way found
            return 0  # No valid way
        
        # Key for memoization (index and current cumulative sum)
        key = (i, curr)
        
        # If result is already computed, return it from the cache
        if key in self.cache:
            return self.cache[key]
        
        # Option 1: Include the current number with a '+' sign
        a = self.count(nums, i + 1, n, curr + nums[i], target)
        
        # Option 2: Include the current number with a '-' sign
        b = self.count(nums, i + 1, n, curr, target)
        
        # Total ways by combining both options
        res = a + b
        
        # Store the result in the cache and return it
        self.cache[key] = res
        return res

    # Main function to calculate the number of ways to assign symbols to achieve the target sum
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)  # Length of the input list
        total = sum(nums)  # Calculate the total sum of all numbers
        
        # Initialize cache for memoization
        self.cache = {}
        
        # Call the recursive function with initial parameters
        return self.count(nums, 0, n, 0, total + target)
