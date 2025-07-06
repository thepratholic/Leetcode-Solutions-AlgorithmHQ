# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import Counter
from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        # Store both lists
        self.nums1 = nums1
        self.nums2 = nums2

        # Create a frequency map for nums2 to help with fast counting
        self.mpp = Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        """
        Add `val` to nums2[index] and update the frequency map accordingly.
        """
        # Decrement the count of the current value at nums2[index]
        self.mpp[self.nums2[index]] -= 1

        # If the count becomes zero, remove it from the map to save space
        if self.mpp[self.nums2[index]] == 0:
            del self.mpp[self.nums2[index]]

        # Add val to nums2[index]
        self.nums2[index] += val

        # Increment the count of the updated value
        self.mpp[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        """
        Count the number of pairs (i, j) such that nums1[i] + nums2[j] == tot
        """
        ans = 0
        for i in range(len(self.nums1)):
            # Target value we need from nums2 to form the sum
            target = tot - self.nums1[i]

            # If target is present in nums2 (using map), add its frequency
            if target in self.mpp:
                ans += self.mpp[target]

        return ans


# Example usage:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index, val)
# param_2 = obj.count(tot)
