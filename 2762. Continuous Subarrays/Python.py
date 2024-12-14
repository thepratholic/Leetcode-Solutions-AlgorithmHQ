from collections import deque

# Stack class with support for maintaining a functional value (like min or max) of the stack.
class Stack:
    def __init__(self, init, func):
        self.stack = deque([(init, init)])  # Store tuples of (value, functional value)
        self.func = func  # Function to compute the property

    def push(self, val):
        top, topfunc = self.stack[-1]  # Get the current top and functional value
        self.stack.append((val, self.func(topfunc, val)))  # Push new value with updated functional value

    def empty(self):
        return len(self.stack) <= 1

    def pop(self):
        if not self.empty():
            top, topfunc = self.stack.pop()  # Remove and return the top value
            return top

    def funcval(self):
        top, topfunc = self.stack[-1]
        return topfunc


# Queue class implemented using two stacks.
class Queue:
    def __init__(self, init=float('inf'), func=min):
        self.func = func  # The function to maintain the property
        self.f = Stack(init, func)  # Forward stack
        self.s = Stack(init, func)  # Reverse stack

    def push(self, val):
        self.f.push(val)

    def empty(self):
        return self.f.empty() and self.s.empty()

    def pop(self):
        if self.s.empty():
            # Transfer all elements from forward stack to reverse stack
            while not self.f.empty():
                self.s.push(self.f.pop())
        if not self.s.empty():
            return self.s.pop()

    def funcval(self):
        return self.func(self.f.funcval(), self.s.funcval())


# Solution class for solving the problem.
class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        n = len(nums)  # Length of the array
        res = 0  # Initialize result

        # Initialize min and max queues
        minq = Queue(float('inf'), func=min)  # Queue to track the minimum value in the current window
        maxq = Queue(float('-inf'), func=max)  # Queue to track the maximum value in the current window

        i = 0  # Left pointer of the sliding window

        # Iterate through the array with the right pointer `j`
        for j in range(n):
            # Add the current element to both min and max queues
            minq.push(nums[j])
            maxq.push(nums[j])

            # Adjust the left pointer `i` to ensure the condition is satisfied
            while i < j and maxq.funcval() - minq.funcval() > 2:
                # Pop elements from both queues and move the left pointer
                minq.pop()
                maxq.pop()
                i += 1

            # The number of valid subarrays ending at index `j` is `(j - i + 1)`
            res += j - i + 1

        return res
