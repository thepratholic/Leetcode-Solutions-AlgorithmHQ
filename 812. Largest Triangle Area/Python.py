# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)

        # Start with the smallest possible value of area
        maxi = float('-inf')

        # Try all triplets of points (brute force)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):

                    # Coordinates of 3 points
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    # Area of triangle using Shoelace Formula:
                    # 0.5 * | x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2) |
                    area = 0.5 * abs(
                        x1 * (y2 - y3) +
                        x2 * (y3 - y1) +
                        x3 * (y1 - y2)
                    )

                    # Keep track of the maximum area found so far
                    maxi = max(maxi, area)

        # Return maximum area among all possible triangles
        return maxi
