# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0

        # Sort points:
        #   1) By x-coordinate ascending
        #   2) If x is the same, then by y-coordinate descending
        # This ensures for same x, higher y comes first.
        points.sort(key=lambda p: (p[0], -p[1]))

        # Outer loop: pick the first point (x1, y1)
        for i in range(n):
            x1, y1 = points[i]

            # Best y-value found so far in comparisons with later points
            bestY = float('-inf')

            # Inner loop: check pairs with later points (x2, y2)
            for j in range(i + 1, n):
                x2, y2 = points[j]

                # Skip if second point's y is higher than the first point's y
                # Because we only want pairs where y2 <= y1
                if y2 > y1:
                    continue

                # If this y2 is larger than any previously seen valid y2,
                # we found a new valid pair
                if y2 > bestY:
                    res += 1
                    bestY = y2   # update best seen y2

        return res
