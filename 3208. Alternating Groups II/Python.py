# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        new_colors = colors + colors[:k - 1]  # Simulate circular behavior without modifying input
        n = len(new_colors)

        count = 0
        l = 0  # Start of the alternating segment

        for r in range(1, n):
            if new_colors[r] == new_colors[r - 1]:  # Break in alternation
                l = r  # Reset the start of the segment

            if r - l + 1 == k:  # Valid window of size k
                count += 1
                l += 1  # Move left to maintain window size

        return count
