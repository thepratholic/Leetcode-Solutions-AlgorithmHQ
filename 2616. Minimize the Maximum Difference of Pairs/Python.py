# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

from typing import List

class Solution:
    # Helper function to check if we can form at least 'p' pairs
    # such that the difference in each pair is <= mid
    def f(self, mid, nums, p):
        cnt = 0
        n = len(nums)
        i = 0

        while i < n - 1:
            # If current pair satisfies the condition
            if nums[i + 1] - nums[i] <= mid:
                cnt += 1
                i += 2  # Move to next possible pair
            else:
                i += 1  # Try next pair starting point

        return cnt >= p  # Return True if enough pairs are formed

    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()  # Sort the array to make pairing adjacent elements easier

        low, high = 0, nums[-1] - nums[0]  # Possible range for the max difference
        ans = float("inf")

        # Binary search to find the minimum possible max difference
        while low <= high:
            mid = (low + high) >> 1  # Mid difference

            if self.f(mid, nums, p):
                # If possible to form p pairs with max difference <= mid
                ans = min(ans, mid)
                high = mid - 1  # Try smaller max difference
            else:
                low = mid + 1  # Increase allowed difference

        return ans  # Final answer: smallest possible max difference
