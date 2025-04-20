# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/thepratholic/

from typing import List

class Solution:
    # Helper function to check if we can repair all 'cars' in 'mid' time
    def f(self, ranks: List[int], cars: int, mid: int) -> bool:
        cnt = 0  # Total cars repaired
        for r in ranks:
            # Number of cars a mechanic with rank 'r' can repair in 'mid' time
            cnt += int((mid // r) ** 0.5)
        return cnt >= cars  # Return True if we can repair all cars

    # Main function to find minimum time to repair all cars
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low, high = 1, max(ranks) * cars * cars  # Define search space
        ans = -1  # Store the minimum valid time

        while low <= high:
            mid = (low + high) >> 1  # Binary search: find middle time
            
            if self.f(ranks, cars, mid):  # Check if 'mid' time is feasible
                ans = mid  # Store current 'mid' as a valid answer
                high = mid - 1  # Try reducing time (move left)
            else:
                low = mid + 1  # Increase time (move right)

        return ans  # Return the minimum valid repair time
