from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float("inf")
        q = deque()
        curSum = 0

        for r in range(len(nums)):
            curSum += nums[r]
            if curSum >= k:
                res = min(res, r + 1)

            while q and curSum - q[0][0] >= k:
                pre, end = q.popleft()
                res = min(res, r - end)


            while q and q[-1][0] > curSum:
                q.pop()
            q.append((curSum, r))

        return -1 if res == float("inf") else res


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/