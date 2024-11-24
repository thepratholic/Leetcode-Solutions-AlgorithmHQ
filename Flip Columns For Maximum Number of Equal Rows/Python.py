from collections import defaultdict
from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = defaultdict(int)  # Dictionary to store counts of row patterns.

        for row in matrix:
            rowKey = str(row)  # Default key for the current row as a string.

            # Flip the row if its first element is 1, to normalize starting from 0.
            if row[0]:
                rowKey = str([0 if n else 1 for n in row])  # Create the flipped pattern.

            count[rowKey] += 1  # Increment the count for the row's pattern.

        return max(count.values())  # Return the maximum count of a single pattern.


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/
