# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)

        odds, evens = 0, 0

        # Count how many even and how many odd numbers are in the list
        for i in nums:
            if i & 1:            # if the number is odd
                odds += 1
            else:                # if the number is even
                evens += 1

        # Now count the longest alternating parity subsequence
        # Start with the first number's parity
        alt = 1
        prev = nums[0] % 2       # 0 for even, 1 for odd

        for i in range(1, n):
            cur = nums[i] % 2
            if cur != prev:      # if parity changes (even <-> odd)
                alt += 1
                prev = cur       # update the previous parity

        # Return the maximum length among all even, all odd, and alternating parity subsequences
        return max(evens, odds, alt)
