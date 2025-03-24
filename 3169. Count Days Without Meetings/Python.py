# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Step 1: Sort meetings based on start time
        meetings.sort()

        free = 0  # Counter for free days
        prev_end = 0  # Track the last meeting's end day

        # Step 2: Traverse through meetings
        for start, end in meetings:
            if start > prev_end + 1:  # If there's a gap before this meeting starts
                free += start - prev_end - 1  # Add free days in between

            # Step 3: Update prev_end to keep track of latest occupied day
            prev_end = max(prev_end, end)

        # Step 4: Add remaining free days after the last meeting
        free += days - prev_end

        return free
