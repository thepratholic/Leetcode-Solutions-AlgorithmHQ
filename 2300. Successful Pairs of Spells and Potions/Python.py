# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)

        # Sort potions to enable binary search
        potions.sort()

        # Helper function to find the first potion index that forms a successful pair with spell[idx]
        def check(idx):
            ans = -1
            low, high = 0, m - 1

            # Binary search on potions array
            while low <= high:
                mid = (low + high) >> 1  # mid = (low + high) // 2

                # If current potion * spell strength >= success threshold,
                # move left to find smaller index (first valid potion)
                if potions[mid] * spells[idx] >= success:
                    ans = mid
                    high = mid - 1

                # Otherwise, move right (need stronger potion)
                else:
                    low = mid + 1

            # If found a valid index, return it; else return m (no valid potion)
            return ans if ans != -1 else m

        # This will store result for each spell
        pairs = [-1] * n

        # For every spell, find how many potions form a successful pair
        for i in range(n):
            # check(i) gives index of the first successful potion
            # total successful potions = m - that index
            pairs[i] = m - check(i)

        return pairs
