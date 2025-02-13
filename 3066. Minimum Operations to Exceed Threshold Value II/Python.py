# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)  # Convert nums into a min-heap (O(n))
        
        min_ops = 0
        while nums[0] < k:  # Only process if the smallest element is < k
            
            x = heapq.heappop(nums)  # Smallest element (O(log n))
            y = heapq.heappop(nums)  # Second smallest element (O(log n))

            new_val = min(x, y) * 2 + max(x, y)  # Given transformation
            heapq.heappush(nums, new_val)  # Push back new value (O(log n))

            min_ops += 1
        
        return min_ops  # Return the number of operations required
