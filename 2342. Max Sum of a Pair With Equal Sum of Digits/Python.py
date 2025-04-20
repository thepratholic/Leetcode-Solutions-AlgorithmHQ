# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict
from typing import List

class Solution:
    def sumOfNumDigits(self, num): # helper function to compute sum of digits of passed number
        ans = 0
        while num > 0:
            ld = num % 10  # Extract the last digit
            ans += ld  # Add it to the sum
            num //= 10  # Remove the last digit
        return ans



    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        mpp = defaultdict(list)  # Dictionary to store numbers grouped by their digit sum

        # Step 1: Group numbers by their digit sum
        for i in range(n):
            ans = self.sumOfNumDigits(nums[i])  # Calculate the sum of digits
            mpp[ans].append(nums[i])  # Store the number in the respective group

        maxi = -1  # Variable to keep track of the maximum sum of any valid pair

        # Step 2: Iterate through the groups and find the max sum of any two numbers
        for k, v in mpp.items():
            if len(v) >= 2:  # Only consider groups with at least 2 numbers
                v.sort(reverse=True)  # Sort numbers in descending order

                ans = v[0] + v[1]  # Take the two largest numbers in the group
                maxi = max(maxi, ans)  # Update the maximum sum if it's greater

        return maxi  # Return the maximum sum found, or -1 if no valid pair exists
