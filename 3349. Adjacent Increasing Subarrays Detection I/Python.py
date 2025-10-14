# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        first, second = False, False  # Flags to track if two consecutive increasing subarrays exist

        # Iterate over possible starting points of the first subarray
        # We need space for two subarrays of size k => loop till n - 2*k
        for i in range(n - 2 * k + 1):

            # ----- Check first subarray from i to i + k - 1 -----
            ptr = i + 1
            first = True  # Assume it's increasing initially
            while ptr < i + k:
                # If current element is greater than previous, still increasing
                if nums[ptr] > nums[ptr - 1]:
                    ptr += 1
                else: 
                    # Found a non-increasing pair → fail
                    first = False
                    break

            # ----- Check second subarray from i + k to i + 2*k - 1 -----
            ptr = i + k + 1
            second = True  # Assume increasing initially
            while ptr < i + 2 * k:
                # Same check for strictly increasing sequence
                if nums[ptr] > nums[ptr - 1]:
                    ptr += 1
                else: 
                    second = False
                    break

            # If both subarrays are strictly increasing → condition satisfied
            if first and second:
                return True

        # If loop completes without finding valid pair → return False
        return False
