# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)  # length of the array

        total_sum = sum(nums)  # total sum of all elements in nums
        left_sum = 0           # keeps track of sum of elements on the left side
        ans = 0                # final count of valid selections

        # iterate through each element of the array
        for i in range(n):
            left_sum += nums[i]            # include current element in left sum
            right_sum = total_sum - left_sum  # remaining sum on the right side

            # only check for positions where current element is 0
            if nums[i] == 0:

                # case 1: if left and right sums are equal
                # -> both left-to-right and right-to-left selections are valid
                if left_sum == right_sum:
                    ans += 2

                # case 2: if the difference between left and right sums is 1
                # -> only one valid selection possible
                elif abs(left_sum - right_sum) == 1:
                    ans += 1

        # return total number of valid selections found
        return ans
