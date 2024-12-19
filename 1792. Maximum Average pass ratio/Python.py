# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/thepratholic/

import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        # Number of classes
        n = len(classes)

        # Lambda function to calculate the difference in pass ratio when an extra student is added.
        diff = lambda a, b: (a + 1) / (b + 1) - a / b

        # Priority queue (max-heap) to store classes based on the largest gain in pass ratio
        # Use negative values because Python's heapq implements a min-heap by default
        heap = []
        for a, b in classes:
            heapq.heappush(heap, (-diff(a, b), a, b))  # Push (-gain, passed, total)

        # Assign extra students one by one to the class with the maximum gain in pass ratio
        for _ in range(extraStudents):
            currdiff, a, b = heapq.heappop(heap)  # Get the class with the maximum gain
            heapq.heappush(heap, (-diff(a + 1, b + 1), a + 1, b + 1))  # Update the class with an extra student

        # Calculate the total average pass ratio after distributing all extra students
        res = 0
        for diff, a, b in heap:
            res += a / b  # Sum up the pass ratios of all classes
        res /= n  # Divide by the number of classes to get the average pass ratio

        return res
