# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        # -------------------------------
        # Step 1: Build prefix array
        # pref[i] = length of increasing subarray ending at index i
        # -------------------------------
        pref = [1] * n  # every element is at least an increasing subarray of length 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:        # if strictly increasing
                pref[i] = pref[i - 1] + 1    # extend the previous increasing subarray
            # else, it remains 1 (since increasing sequence broke)

        # -------------------------------
        # Step 2: Build suffix array
        # suff[i] = length of increasing subarray starting at index i
        # -------------------------------
        suff = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:        # if strictly increasing
                suff[i] = suff[i + 1] + 1    # extend the increasing subarray towards right
            # else, it remains 1

        # -------------------------------
        # Step 3: Find the maximum size of two consecutive increasing subarrays
        # The idea is:
        # For a split point between i and i+1,
        #   - left side ends at i  → has pref[i] length
        #   - right side starts at i+1 → has suff[i+1] length
        # To form two consecutive increasing subarrays, both sides
        # must have at least that many elements.
        # So we take min(pref[i], suff[i+1]) at each split.
        # -------------------------------
        ans = 0
        for i in range(n - 1):
            ans = max(ans, min(pref[i], suff[i + 1]))

        # -------------------------------
        # Step 4: Return final answer
        # -------------------------------
        return ans
