from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # Step 1: Identify the rightmost point where the array is non-decreasing.
        right = len(arr) - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1  # Move left until the sequence starts decreasing

        # Step 2: Initialize the answer as the length of the subarray from 0 to 'right'
        ans = right

        # Step 3: Initialize left pointer to the start of the array.
        left = 0
        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            # Step 4: Expand the right pointer while the current left element is greater than the right element
            while right < len(arr) and arr[left] > arr[right]:
                right += 1  # Move the right pointer to the right position

            # Step 5: Update the answer with the minimal subarray length
            ans = min(ans, right - left - 1)
            left += 1  # Move the left pointer to the next element

        return ans  # Return the length of the shortest subarray to remove


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/
