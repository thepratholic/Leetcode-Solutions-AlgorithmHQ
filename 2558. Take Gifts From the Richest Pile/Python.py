import heapq
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        # Initialize max-heap with negative values
        for el in gifts:
            heapq.heappush(heap, -el)

        # Perform `k` operations
        for _ in range(k):
            v = -heapq.heappop(heap)  # Extract max value (negated back to positive)
            heapq.heappush(heap, -int(v ** 0.5))  # Push the square root (negated again)

        # Return the total sum of the gifts
        return -sum(heap)
