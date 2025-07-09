# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        free_times = []  # Will store all the free time gaps
        ans = 0
        n = len(startTime)

        # Time from beginning (0) to first event's start
        free_times.append(startTime[0] - 0)

        # Time between consecutive events
        for i in range(1, n):
            free_times.append(startTime[i] - endTime[i - 1])

        # Time from end of last event to end of total time
        free_times.append(eventTime - endTime[-1])

        # Now use a sliding window of size k+1 (as skipping k events gives k+1 free intervals)
        l, r = 0, 0
        maxi = float('-inf')
        cur = 0  # Current sum of free times in the window

        while r < len(free_times):
            cur += free_times[r]

            # Shrink the window if it exceeds size k+1
            if r - l + 1 > k + 1:
                while r - l + 1 > k + 1:
                    cur -= free_times[l]
                    l += 1

            # Update the maximum free time sum found so far
            maxi = max(maxi, cur)
            r += 1

        return maxi
