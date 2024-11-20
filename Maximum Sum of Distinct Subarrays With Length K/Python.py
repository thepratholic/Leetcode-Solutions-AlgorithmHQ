from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, 0
        maxSum, curr = 0, 0
        s = set()

        for r in range(n):
            while nums[r] in s:
                s.remove(nums[l])
                curr -= nums[l]
                l += 1

            s.add(nums[r])
            curr += nums[r]

            if r - l + 1 == k:
                maxSum = max(maxSum, curr)
                s.remove(nums[l])
                curr -= nums[l]
                l += 1

        return maxSum


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/