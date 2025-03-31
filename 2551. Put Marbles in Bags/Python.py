# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)

        splits = []

        for i in range(n - 1):
            splits.append(weights[i] + weights[i + 1])

        splits.sort()

        mini, maxi = 0, 0

        for i in range(k-1):
            mini += splits[i]
            maxi += splits[-(i + 1)]

        return maxi - mini