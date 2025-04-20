from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)  # Total number of elements in the list
        cnt = 0  # Counter to keep track of valid pairs

        # Brute-force approach: check all pairs (i, j) such that i < j
        for i in range(n - 1):
            for j in range(i + 1, n):
                # Check if both conditions are satisfied:
                # 1. nums[i] == nums[j]  (same values)
                # 2. (i * j) is divisible by k
                if nums[i] == nums[j] and ((i * j) % k) == 0:
                    cnt += 1  # Valid pair found

        return cnt  # Return the total number of valid pairs
