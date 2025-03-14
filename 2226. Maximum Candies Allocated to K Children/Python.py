# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def f(self, candies, k, mid):
        cnt = 0
        for i in candies:
            cnt += (i // mid)  # Count how many children can get at least `mid` candies
        return cnt >= k
    
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low, high, ans = 1, max(candies), 0  # Search space
        
        while low <= high:
            mid = (low + high) >> 1  # Middle value
            
            if self.f(candies, k, mid):  # Can we distribute at least `k` candies?
                ans = mid  # Store the valid mid
                low = mid + 1  # Search for a larger valid mid
            else:
                high = mid - 1  # Reduce search space

        return ans