# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        n = len(nums)
        total = 1 << n  # Total number of subsets = 2^n (using bitmasking)

        max_or = 0  # To store the maximum OR value found among all subsets
        count = 0   # To count how many subsets produce the maximum OR value

        # Iterate through all possible subsets represented as bitmasks
        for mask in range(total):
            cur_or = 0  # OR value of the current subset

            # For each bit in the mask, check if the i-th element is included
            for i in range(n):
                if mask & (1 << i):  # If the i-th bit is set in mask
                    cur_or |= nums[i]  # Include nums[i] in OR calculation

            # If current OR is greater than max_or, update max_or and reset count
            if cur_or > max_or:
                max_or = cur_or
                count = 1  # Only one subset found so far with this new max_or
            elif cur_or == max_or:
                count += 1  # Found another subset with same max_or

        return count  # Return the total number of subsets with maximum OR
