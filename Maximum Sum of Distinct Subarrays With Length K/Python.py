from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, 0
        maxSum, curr = 0, 0  # `maxSum` stores the maximum sum, `curr` is the current window sum.
        s = set()  # Set to store unique elements in the current window.

        for r in range(n):
            # Shrink the window from the left until `nums[r]` is unique.
            while nums[r] in s:
                s.remove(nums[l])
                curr -= nums[l]
                l += 1

            s.add(nums[r])
            curr += nums[r]

            # When the window size matches `k`, check and update the maximum sum.
            if r - l + 1 == k:
                maxSum = max(maxSum, curr)  # Update the maximum sum if the current sum is larger.
                # Shrink the window from the left to maintain size `k` for subsequent iterations.
                s.remove(nums[l])
                curr -= nums[l]
                l += 1

        return maxSum


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/
