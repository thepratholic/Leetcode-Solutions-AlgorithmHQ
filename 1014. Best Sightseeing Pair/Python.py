# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)  # Number of attractions
        mleft = float('-inf')  # Tracks the maximum value of (values[i] + i) so far
        res = float('-inf')  # Stores the maximum score found so far

        # Iterate through all attractions
        for i in range(n):
            # Calculate the current score using the best left value and the current attraction
            res = max(res, mleft + values[i] - i)

            # Update mleft to the maximum value of (values[i] + i)
            mleft = max(mleft, values[i] + i)

        # Return the maximum score found
        return res
