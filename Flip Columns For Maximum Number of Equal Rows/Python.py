from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = defaultdict(int)
        for row in matrix:
            rowKey = str(row)

            if row[0]:
                rowKey = str([0 if n else 1 for n in row])

            count[rowKey] += 1
        return max(count.values())


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/