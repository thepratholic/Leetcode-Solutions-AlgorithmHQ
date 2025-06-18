# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()  # Sort the array in ascending order

        ans = []     # This will store the groups
        n = len(nums)

        i = 0
        while i < n - 2:  # Process every 3 elements
            tmp = [nums[i], nums[i + 1], nums[i + 2]]

            # If the difference between the largest and smallest in the triplet is more than k,
            # it's not possible to make valid groups.
            if tmp[2] - tmp[0] > k:
                return []

            ans.append(tmp)  # Add the valid triplet to the result
            i += 3           # Move to the next triplet

        return ans  # Return the list of groups
