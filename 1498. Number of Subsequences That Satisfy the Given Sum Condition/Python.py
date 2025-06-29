from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        M = 10 ** 9 + 7  # Modulo value to prevent integer overflow
        nums.sort()      # Sort the array to apply two-pointer technique
        n = len(nums)

        # Precompute powers of 2 up to length n using modulo M
        power = [-1] * n
        power[0] = 1
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % M

        # Initialize two pointers
        l, r = 0, n - 1
        ans = 0

        # Two-pointer approach
        while l <= r:
            if nums[l] + nums[r] <= target:
                # All subsequences between l and r (where nums[l] is min, nums[r] is max)
                ans += power[r - l] % M
                l += 1
            else:
                # If sum exceeds target, we need to reduce the max (move r)
                r -= 1

        return ans % M
