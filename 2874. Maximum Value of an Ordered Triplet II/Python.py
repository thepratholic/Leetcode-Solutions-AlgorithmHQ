from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)

        res, i_maxi, d_maxi = 0, 0, 0  # Initialize result and helper variables

        for k in range(n):  # Iterate through the array
            # Step 3: Compute the final triplet value using previously stored values
            res = max(res, nums[k] * d_maxi)

            # Step 2: Update d_maxi (max(nums[i] - nums[j]))
            d_maxi = max(d_maxi, i_maxi - nums[k])

            # Step 1: Update i_maxi (max(nums[i]) seen so far)
            i_maxi = max(i_maxi, nums[k])

        return res
