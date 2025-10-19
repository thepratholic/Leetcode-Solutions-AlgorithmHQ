# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # BFS queue initialized with the original string
        q = deque([s])

        # Set to track visited configurations to avoid repetition
        vis = set()

        # Keep track of the lexicographically smallest string found
        smallest = s

        while q:
            cur = q.popleft()

            # Skip if we've already seen this configuration
            if cur in vis:
                continue

            vis.add(cur)

            # Update the smallest string found so far
            smallest = min(smallest, cur)

            # ----------------------------
            # Operation 1: Add 'a' to all digits at odd indices
            # ----------------------------
            l = list(cur)
            n = len(l)

            for i in range(1, n, 2):  # Only odd indices
                cur_num = int(l[i])
                cur_num = (cur_num + a) % 10  # Perform addition modulo 10
                l[i] = str(cur_num)

            added = "".join(l)

            # ----------------------------
            # Operation 2: Rotate the string to the right by 'b' positions
            # ----------------------------
            rotated = cur[-b:] + cur[:-b]

            # Push both possible next states into the queue (if unseen)
            for nxt in [added, rotated]:
                if nxt not in vis:
                    q.append(nxt)

        # Return the lexicographically smallest string encountered
        return smallest
