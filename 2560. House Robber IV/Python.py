# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/thepratholic/

from typing import List

class Solution:
    def f(self, nums, k, mid):
        cnt = 0
        i = 0
        while i < len(nums):
            if nums[i] <= mid:
                cnt += 1
                i += 2  # Skip adjacent house
            else:
                i += 1  # Move to next house
        return cnt >= k
    
    def minCapability(self, nums: List[int], k: int) -> int:
        ans = -1
        low, high = 0, max(nums)

        while low <= high:
            mid = (low + high) >> 1  # Binary search mid-point

            if self.f(nums, k, mid):  # Can we rob `k` houses with max `mid`?
                ans = mid  # Store valid answer
                high = mid - 1  # Try smaller `mid`
            else:
                low = mid + 1  # Increase `mid` (not enough houses robbed)

        return ans

