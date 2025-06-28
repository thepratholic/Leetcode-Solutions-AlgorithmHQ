# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        
        values = []

        # Step 1: Pair each element with its index
        for index, element in enumerate(nums):
            values.append((index, element))  # (original_index, value)

        # Step 2: Sort by value in descending order to get the k largest elements
        values.sort(key = lambda x : x[1], reverse = True)

        # Step 3: From the top-k largest values, restore their original order by sorting by index
        values = sorted(values[:k])  # sort back by original index

        # Step 4: Extract only the values (not indices) to return the final subsequence
        return [v for i, v in values]
