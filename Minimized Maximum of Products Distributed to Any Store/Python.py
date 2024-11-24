from typing import List

class Solution:
    def can_distribute(self, x: int, quantities: List[int], n: int) -> bool:
        j = 0
        remaining = quantities[j]

        for i in range(n):  # Iterate over the stores.
            if remaining <= x:  # If the current store can take all remaining items:
                j += 1  # Move to the next quantity.
                if j == len(quantities):  # All quantities are distributed successfully.
                    return True
                remaining = quantities[j]  # Reset remaining to the next quantity.
            else:
                remaining -= x  # Distribute `x` items to the current store.

        return False  # Not all quantities can be distributed.

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 1
        right = max(quantities)

        while left < right:
            middle = (left + right) // 2
            # Check if `middle` can be the maximum items per store.
            if self.can_distribute(middle, quantities, n):
                right = middle
            else:
                left = middle + 1

        return left  # The minimized maximum value.


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/
