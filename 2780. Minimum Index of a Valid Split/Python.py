from collections import defaultdict
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)

        # 'first' will store the frequency of each element in the prefix (from start to current index)
        first = defaultdict(int)
        # 'second' will store the frequency of each element in the suffix (from current index+1 to end)
        second = defaultdict(int)

        # Initially, fill 'second' with the frequency of each element in the entire array
        for i in nums:
            second[i] += 1

        # Traverse the array and update 'first' and 'second' counts accordingly
        for i in range(n):
            # Update the frequency: remove nums[i] from the suffix and add it to the prefix
            second[nums[i]] -= 1
            first[nums[i]] += 1

            # Check if the element at index i becomes the majority element in both parts:
            # - In the prefix (first i+1 elements), the frequency of nums[i] should be more than half.
            # - In the suffix (remaining n - i - 1 elements), the frequency of nums[i] should be more than half.
            if first[nums[i]] * 2 > i + 1 and second[nums[i]] * 2 > n - i - 1:
                return i  # Return the first index where the condition holds

        # If no such index exists, return -1
        return -1
