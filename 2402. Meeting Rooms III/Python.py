# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        # Room usage count
        used_rooms_count = [0] * n

        # Min-heap for room availability: (end_time, room_index)
        busy_rooms = []

        # Min-heap for available room indices
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)

        for start, end in meetings:
            # Free up all rooms that are done before current meeting starts
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms, room)

            duration = end - start

            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(busy_rooms, (end, room))
                used_rooms_count[room] += 1
            else:
                # No room is free, delay meeting to the earliest available time
                earliest_end_time, room = heapq.heappop(busy_rooms)
                new_end = earliest_end_time + duration
                heapq.heappush(busy_rooms, (new_end, room))
                used_rooms_count[room] += 1

        # Find the room used most often (with smallest index if tie)
        max_used = max(used_rooms_count)
        for i in range(n):
            if used_rooms_count[i] == max_used:
                return i