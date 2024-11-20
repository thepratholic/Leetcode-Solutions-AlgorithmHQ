from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        cnt = 1
        n = len(nums)
        l = 0
        for r in range(n):
            if r > 0 and nums[r - 1] + 1 == nums[r]:
                cnt += 1

            if r - l + 1 > k:
                if nums[l] + 1 == nums[l + 1]:
                    cnt -= 1
                l += 1

            if r - l + 1 == k:
                res.append(nums[r] if cnt == k else -1)

        return res


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/