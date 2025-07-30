# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        maxi = max(nums)  # Find the maximum value in the array

        longest = float('-inf')  # Will store the length of the longest subarray of max elements
        current = 0  # Current streak of consecutive max elements

        # Traverse through each element in the array
        for element in nums:
            if element == maxi:
                current += 1  # Increment streak if current element is the maximum
                longest = max(longest, current)  # Update the longest if needed
            else:
                current = 0  # Reset streak if element is not the maximum

        return longest  # Return the length of the longest subarray of max elements
