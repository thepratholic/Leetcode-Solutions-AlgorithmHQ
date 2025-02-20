# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)  # The number of binary strings (and also the length of each string)
        res = ""      # This will store the result string

        # We iterate over each index from 0 to n-1.
        # By flipping the i-th character of the i-th string,
        # we ensure that the resulting string differs from every string in nums.
        for i in range(n):
            # If the i-th character in the i-th string is "1", choose "0"; otherwise, choose "1".
            ch = "0" if nums[i][i] == "1" else "1"
            res += ch  # Append the chosen character to the result

        return res  # Return the constructed binary string
