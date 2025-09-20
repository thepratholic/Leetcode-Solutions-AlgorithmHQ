# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from collections import deque, defaultdict
from bisect import bisect_left, bisect_right, insort
from typing import List

class Router:
    def __init__(self, memoryLimit: int):
        # Max number of packets the router can hold
        self.memoryLimit = memoryLimit

        # FIFO queue to store packets (used for eviction and forwarding in order of arrival)
        self.storage = deque()            

        # Set for O(1) duplicate detection of packets (source, destination, timestamp)
        self.packet_set = set()         

        # Dictionary: destination → sorted list of timestamps
        # Helps in efficient range queries (getCount)
        self.dest_map = defaultdict(list) 

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        """
        Adds a new packet if it is not duplicate and memory is available.
        If memory is full, evicts the oldest packet.
        Returns True if added, False if rejected.
        """
        packet = (source, destination, timestamp)

        # Reject if packet already exists (duplicate)
        if packet in self.packet_set:
            return False

        # If memory full → evict the oldest packet
        if len(self.storage) >= self.memoryLimit:
            old_src, old_dest, old_ts = self.storage.popleft()   # remove oldest packet
            self.packet_set.discard((old_src, old_dest, old_ts)) # remove from set

            # Remove timestamp from destination mapping
            arr_old = self.dest_map[old_dest]
            idx_old = bisect_left(arr_old, old_ts)
            if idx_old < len(arr_old) and arr_old[idx_old] == old_ts:
                arr_old.pop(idx_old)
            if not arr_old:
                del self.dest_map[old_dest]   # cleanup empty list

        # Add new packet
        self.storage.append(packet)
        self.packet_set.add(packet)

        # Insert timestamp in sorted order for destination
        insort(self.dest_map[destination], timestamp)

        return True

    def forwardPacket(self) -> List[int]:
        """
        Forwards (removes and returns) the oldest packet from storage.
        If empty, return [].
        """
        if not self.storage:
            return []

        # Remove oldest packet
        source, destination, timestamp = self.storage.popleft()
        self.packet_set.discard((source, destination, timestamp))

        # Remove timestamp from destination mapping
        arr = self.dest_map[destination]
        idx = bisect_left(arr, timestamp)
        if idx < len(arr) and arr[idx] == timestamp:
            arr.pop(idx)
        if not arr:
            del self.dest_map[destination]

        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        """
        Returns the number of packets for a given destination
        whose timestamps are in [startTime, endTime].
        """
        if destination not in self.dest_map:
            return 0

        arr = self.dest_map[destination]   # sorted list of timestamps

        # Find leftmost index ≥ startTime
        left = bisect_left(arr, startTime)

        # Find rightmost index > endTime
        right = bisect_right(arr, endTime)

        return right - left
