# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        pos, neg = 0, 0 # to count number of positives and negative values

        for i in range(n):
            if nums[i] == 0: # if we encounter zero, then we must not count it
                continue

            if nums[i] < 0: # counting number of negatives
                neg += 1
            else:
                pos += 1 # counting number of ones

        return max(pos, neg) # return maximum of positives and negatives