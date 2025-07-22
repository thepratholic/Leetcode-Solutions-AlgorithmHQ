from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # Edge case: only one element
        if n == 1:
            return nums[0]

        st = set()        # To store unique elements in the current window
        l = r = 0         # Two pointers for sliding window
        sum_ = 0          # Current window sum
        maxi = float('-inf')  # Max sum of all valid windows

        while r < n:
            # If duplicate found, move left pointer to remove duplicates
            if nums[r] in st:
                while l <= r and nums[l] != nums[r]:
                    sum_ -= nums[l]
                    st.discard(nums[l])
                    l += 1

                # Remove the duplicate itself
                sum_ -= nums[l]
                st.discard(nums[l])
                l += 1

            # Now nums[r] is unique in the window
            sum_ += nums[r]
            st.add(nums[r])
            maxi = max(maxi, sum_)
            r += 1

        return maxi