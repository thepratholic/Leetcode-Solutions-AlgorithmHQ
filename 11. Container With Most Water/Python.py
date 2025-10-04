# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        # Two pointers approach:
        # i -> left pointer (start)
        # j -> right pointer (end)
        i = 0
        j = n - 1

        ans = float('-inf')  # to store the maximum area found

        # While the two pointers haven't met
        while i < j:
            # Calculate area:
            # Width = (j - i)
            # Height = min(height[i], height[j])  -> the shorter one limits the water height
            ans = max(ans, (j - i) * min(height[i], height[j]))

            # Move the pointer which has smaller height inward
            # because a taller line may form a bigger area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        # Return the maximum area found
        return ans
