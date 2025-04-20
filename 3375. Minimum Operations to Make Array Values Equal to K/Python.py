# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from collections import defaultdict
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)  # Length of the input array (not directly used)

        mpp = defaultdict(int)  # Create a dictionary to count the frequency of each number
        
        # Build the frequency map
        for i in nums:
            mpp[i] += 1

        ops = 0  # Initialize the number of operations needed

        # Iterate through all unique elements in the map
        for e in mpp.keys():
            if e > k:
                ops += 1  # If element is greater than k, increment operation count
            if e < k:
                return -1  # If any element is less than k, return -1 immediately (cannot fix)

        return ops  # Return the total operations needed
