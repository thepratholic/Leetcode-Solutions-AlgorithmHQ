from typing import List


class Solution:
    def can_distribute(self, x: int, quantities: List[int], n: int) -> bool:
        j = 0
        remaining = quantities[j]

        for i in range(n):
            if remaining <= x:

                j += 1
                if j == len(quantities):
                    return True
                else:
                    remaining = quantities[j]
            else:
                remaining -= x

        return False

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 0
        right = max(quantities)

        while left < right:
            middle = (left + right) // 2
            if self.can_distribute(middle, quantities, n):
                right = middle
            else:

                left = middle + 1

        return left



# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/