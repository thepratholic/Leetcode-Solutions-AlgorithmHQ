# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List
from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)

        # Initialize the answer array with 1s (default for drying days)
        ans = [1] * n

        # Keeps indices of days when it doesn't rain (potential dry days)
        dry_days = SortedList()

        # Stores the last day when each lake was filled with rain
        last_rain = {}

        # Iterate over all days
        for i, lake in enumerate(rains):

            # Case 1: No rain today → can dry any lake later
            if lake == 0:
                dry_days.add(i)

            # Case 2: It rains over lake 'lake' today
            else:

                # If the lake was already filled before → we must dry it before today
                if lake in last_rain:
                    prev = last_rain[lake]  # The last day this lake got rain

                    # Find the first available dry day *after* that previous rain day
                    idx = dry_days.bisect_right(prev)

                    # If no such dry day exists → flood cannot be avoided
                    if idx == len(dry_days):
                        return []

                    # Use that dry day to dry this lake
                    dry_day = dry_days[idx]

                    ans[dry_day] = lake  # On that dry day, we dry this specific lake
                    dry_days.remove(dry_day)  # Remove that dry day (used now)

                # Update last day when this lake was filled
                last_rain[lake] = i

                # Mark current day as raining → cannot dry any lake
                ans[i] = -1

        # Return the constructed answer
        return ans
