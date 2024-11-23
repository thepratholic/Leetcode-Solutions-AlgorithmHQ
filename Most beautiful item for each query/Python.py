from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()

        # Pair each query with its original index for mapping the results back later.
        queries = sorted([(q, i) for i, q in enumerate(queries)])

        res = [0] * len(queries)  # Result array to store maximum beauty for each query.
        max_bea = 0
        j = 0

        for q, i in queries:
            # Process all items with a price less than or equal to the current query value.
            while j < len(items) and items[j][0] <= q:
                max_bea = max(max_bea, items[j][1])  # Update maximum beauty encountered.
                j += 1  # Move to the next item.

            res[i] = max_bea  # Store the result for the current query.

        return res


# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/
