# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        
        # Find the maximum day up to which events can happen
        max_day = max(event[1] for event in events)

        # Sort the events based on their starting day
        events.sort()

        pq = []  # Min-heap to store end days of available events
        count = 0  # To count how many events we can attend
        j = 0  # Pointer to iterate through events

        # Loop through each day from 1 to the last possible event day
        for day in range(1, max_day + 1):

            # Add all events that start on or before the current day
            while j < n and events[j][0] <= day:
                heapq.heappush(pq, events[j][1])  # Push end day into heap
                j += 1

            # Remove events from the heap that have already ended
            while pq and pq[0] < day:
                heapq.heappop(pq)

            # Attend the event with the earliest end day
            if pq:
                heapq.heappop(pq)
                count += 1

        return count
