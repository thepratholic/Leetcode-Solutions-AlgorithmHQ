# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n = len(s)
        
        # Initialize counters for each direction
        north = west = south = east = maxi = 0

        for i in range(n):
            # Count how many steps in each direction
            if s[i] == "N":
                north += 1
            elif s[i] == "E":
                east += 1
            elif s[i] == "S":
                south += 1
            elif s[i] == "W":
                west += 1

            # Calculate current net Manhattan distance from the origin
            current_dist = abs(north - south) + abs(east - west)

            # Calculate how many steps have been 'wasted'
            # (i+1 total steps taken so far minus actual distance moved)
            wasted_steps = (i + 1) - current_dist

            # You can use up to k corrections,
            # each correction can remove up to 2 wasted steps (one backward and one forward)
            extra = 0
            if wasted_steps != 0:
                extra = min(2 * k, wasted_steps)

            # Update the maximum possible distance with extra corrections used optimally
            maxi = max(maxi, current_dist + extra)

        return maxi
