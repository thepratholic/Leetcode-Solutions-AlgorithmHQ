# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from collections import deque
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]],
                   containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        candiesCollected = 0              # Total candies collected
        visited = set()                   # Set of boxes that have already been opened
        foundBoxes = set()                # Set of all boxes we have discovered

        q = deque()                       # Queue for boxes we can currently open and process

        # First, add all initial boxes to foundBoxes
        for b in initialBoxes:
            foundBoxes.add(b)
            if status[b] == 1:            # If the box is unlocked (can be opened)
                q.append(b)              # Add it to the queue to process
                visited.add(b)           # Mark it as visited (opened)
                candiesCollected += candies[b]  # Collect candies from this box

        # Process all the boxes we can open
        while q:
            box = q.popleft()            # Take out a box from the queue

            # Go through all boxes inside the current box
            for insideBox in containedBoxes[box]:
                foundBoxes.add(insideBox)  # Mark the box as found
                # If the inside box is unlocked and not visited yet
                if status[insideBox] == 1 and insideBox not in visited:
                    q.append(insideBox)
                    visited.add(insideBox)
                    candiesCollected += candies[insideBox]

            # Go through all keys we get from the current box
            for boxKey in keys[box]:
                status[boxKey] = 1  # Mark the box as now unlocked
                # If we already found this box earlier but it was locked, now we can open it
                if boxKey in foundBoxes and boxKey not in visited:
                    q.append(boxKey)
                    visited.add(boxKey)
                    candiesCollected += candies[boxKey]

        return candiesCollected
