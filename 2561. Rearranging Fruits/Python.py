# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # Step 1: Count how many times each fruit appears more in basket1 than basket2 and vice versa
        fruit_diff = Counter()
        min_value = float('inf')  # to track the smallest fruit value

        for fruit in basket1:
            fruit_diff[fruit] += 1
            min_value = min(min_value, fruit)
        
        for fruit in basket2:
            fruit_diff[fruit] -= 1
            min_value = min(min_value, fruit)

        # Step 2: Check if it's possible to make baskets equal
        to_swap = []
        for fruit, count in fruit_diff.items():
            if count % 2 != 0:
                return -1  # not possible if the difference is odd
            # Add half the difference to the list (only one basket needs to swap half the time)
            to_swap.extend([fruit] * (abs(count) // 2))

        if not to_swap:
            return 0  # already same baskets

        to_swap.sort()
        n = len(to_swap) // 2

        # Step 3: Calculate the minimum cost of swapping
        cost = 0
        for i in range(n):
            # Either pay the cost of the current fruit, or double the minimum fruit (better to swap with smallest)
            cost += min(to_swap[i], 2 * min_value)

        return cost
