# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        pq = []  # Min-heap to store characters along with their negative index

        for i, ch in enumerate(s):
            if ch != '*':
                # Push the character and its negative index to preserve original order
                heapq.heappush(pq, (ch, -i))
            else:
                # Pop the lexicographically smallest character seen so far
                heapq.heappop(pq)

        # Reconstruct the result by sorting the heap based on original indices (negative index used for original order)
        return "".join(ch for ch, _ in sorted(pq, key=lambda x: -x[1]))
