from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        res = 0          # Variable to store the total sum of absolute values
        neg_cnt = 0      # Count of negative numbers in the matrix
        mat_min = float("inf")  # Smallest absolute value in the matrix

        # Step 1: Iterate through the matrix
        for row in matrix:
            for n in row:
                res += abs(n)  # Add the absolute value of the element to the total sum
                mat_min = min(mat_min, abs(n))  # Track the smallest absolute value
                if n < 0:  # Count negative numbers
                    neg_cnt += 1

        # Step 2: Adjust the sum if there's an odd number of negatives
        if neg_cnt % 2 == 1:
            # If the count of negatives is odd, subtract twice the smallest absolute value
            res -= 2 * mat_min

        return res

# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/