# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        cnt = 1
        n = len(nums)
        l = 0

        for r in range(n):
            # Check if the current number and the previous number are consecutive.
            if r > 0 and nums[r - 1] + 1 == nums[r]:
                cnt += 1  # Increment consecutive count.

            # If the window size exceeds `k`, shrink it from the left.
            if r - l + 1 > k:
                # If the element leaving the window was part of a consecutive sequence, decrement the count.
                if nums[l] + 1 == nums[l + 1]:
                    cnt -= 1
                l += 1

            # If the current window size is exactly `k`, determine the result for this window.
            if r - l + 1 == k:
                # Append the last number in the window if all `k` numbers are consecutive, otherwise append -1.
                res.append(nums[r] if cnt == k else -1)

        return res
