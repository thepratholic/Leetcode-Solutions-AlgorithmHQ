# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

import heapq
from collections import defaultdict
from typing import List

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # Priority Queue (Min-Heap in Python, so we store negative values
        # to simulate a Max-Heap)
        self.pq = []

        # task_map keeps track of the "latest valid" priority & userId for each taskId
        # { taskId → (priority, userId) }
        self.task_map = defaultdict(tuple)

        # Initialize with given tasks
        for user_id, task_id, priority in tasks:
            # Push into heap with:
            #   -priority → higher priority tasks come first
            #   -task_id  → in case of tie, larger taskId comes first
            #   user_id   → to identify which user owns the task
            heapq.heappush(self.pq, (-priority, -task_id, user_id))

            # Store the latest info in task_map
            self.task_map[task_id] = (priority, user_id)


    def add(self, userId: int, taskId: int, priority: int) -> None:
        # Add a new task into heap & update task_map
        heapq.heappush(self.pq, (-priority, -taskId, userId))
        self.task_map[taskId] = (priority, userId)


    def edit(self, taskId: int, newPriority: int) -> None:
        # Only edit if task exists
        if taskId in self.task_map:
            user_id = self.task_map[taskId][1]   # keep same userId
            # Update task_map with new priority
            self.task_map[taskId] = (newPriority, user_id)
            # Push new entry into heap (lazy deletion, old entry will be skipped later)
            heapq.heappush(self.pq, (-newPriority, -taskId, user_id))


    def rmv(self, taskId: int) -> None:
        # Remove task logically by deleting from task_map
        # Old entries still exist in heap but will be ignored later
        if taskId in self.task_map:
            del self.task_map[taskId]


    def execTop(self) -> int:
        # Keep popping until we find a valid (latest) task
        while self.pq:
            curr_priority, curr_taskId, curr_userId = heapq.heappop(self.pq)

            # Restore original values (since we stored negatives)
            taskId = -curr_taskId
            priority = -curr_priority

            # Check if this entry is still valid in task_map
            if taskId in self.task_map and self.task_map[taskId][0] == priority:
                # Get userId
                userId = self.task_map[taskId][1]
                # Remove task from active map (executed)
                del self.task_map[taskId]
                return userId   # return userId who owns this top task

        # If no tasks left
        return -1


# Example usage:
# obj = TaskManager([[1, 101, 5], [2, 102, 7]])
# obj.add(3, 103, 6)
# obj.edit(101, 8)
# obj.rmv(102)
# print(obj.execTop())  # should execute task 101 (highest priority 8)
