# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from bisect import bisect_left, bisect_right
from typing import List
from collections import Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)

        # Stores the maximum possible frequency we can achieve
        maxi = float('-inf')

        # Sort the array to use binary search and handle ranges efficiently
        nums.sort()

        # Frequency map of each element in nums
        freq = Counter(nums)

        # Use a set to hold all potential target values
        # (each element itself, and +/- k range around it)
        s = set()
        for el in nums:
            s.add(el)
            s.add(el - k)
            s.add(el + k)

        # For every possible target element in the set
        for el in s:
            # Count how many numbers in nums can be converted to this value
            # by adding/subtracting at most k
            count = bisect_right(nums, el + k) - bisect_left(nums, el - k)

            # The frequency of el itself + min(extra elements we can adjust, available operations)
            maxi = max(maxi, freq[el] + min(count - freq[el], numOperations))

        # Return the maximum achievable frequency
        return maxi