# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


import math
from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dim: List[List[int]]) -> int:
        n = len(dim)
        ans = -1
        maxi = float('-inf')

        for l, w in dim:
            v = (l * l) + (w * w) # taking the diagonal length
            area = l * w # area of the rectangle
            diag_length = math.sqrt(v)

            if diag_length > maxi: # if it is greater
                maxi = diag_length
                ans = l * w

            elif diag_length == maxi: # if it is equal, then take the max area
                ans = max(ans, area)
        return ans # return the best ans