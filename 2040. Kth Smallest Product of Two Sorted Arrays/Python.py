# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from bisect import bisect_right, bisect_left
from typing import List

class Solution:
    # Helper function to count how many products with nums1[i] are <= v
    def f(self, nums2, x1, v):
        if x1 > 0:
            # For positive x1: find how many y in nums2 such that x1 * y <= v
            return bisect_right(nums2, v // x1)
        elif x1 < 0:
            # For negative x1: inequality flips, we find how many y such that y >= ceil(v / x1)
            return len(nums2) - bisect_left(nums2, -(-v // x1))  # Equivalent to ceil division
        else:
            # If x1 is zero, all products are 0, so count all if v >= 0, else 0
            return len(nums2) if v >= 0 else 0

    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1 = len(nums1)

        # Binary search over possible values of product
        left, right = -(10**10), 10**10

        while left <= right:
            mid = (left + right) // 2
            count = 0  # Count of products <= mid

            # For each x in nums1, count how many products x * y <= mid
            for i in range(n1):
                count += self.f(nums2, nums1[i], mid)

            # If count is less than k, we need larger products
            if count < k:
                left = mid + 1
            else:
                # mid might be the answer, but try to find smaller
                right = mid - 1

        # left is the smallest product such that at least k products are <= left
        return left
