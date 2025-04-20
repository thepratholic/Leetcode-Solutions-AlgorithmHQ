# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from collections import defaultdict
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = defaultdict(int)  # Track remaining spots in current groups of size ans + 1
        total = 0  # Total number of rabbits

        for ans in answers:
            if ans == 0:
                # If rabbit says 0, it is alone
                total += 1
            elif count[ans] == 0:
                # Need to start a new group of (ans + 1) rabbits
                total += ans + 1
                count[ans] = ans  # One rabbit spoke, so ans more can still say the same
            else:
                # Fill current group
                count[ans] -= 1

        return total
