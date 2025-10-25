# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def totalMoney(self, n: int) -> int:
        days = n          # Total number of days we have
        week = 1          # Start from the first week
        ans = 0           # Variable to store the total amount saved

        # Continue until all days are processed
        while days > 0:

            # Each week starts with 'week' dollars on Monday,
            # then increases by 1 each day for 7 days.
            # For example:
            # week 1 → 1, 2, 3, 4, 5, 6, 7
            # week 2 → 2, 3, 4, 5, 6, 7, 8
            # week 3 → 3, 4, 5, 6, 7, 8, 9
            for money in range(week, week + 7):
                ans += money   # Add today's saving
                days -= 1      # One day completed

                # Stop if we've reached the total number of given days
                if days == 0:
                    break

            # Move to the next week (starting amount increases by 1)
            week += 1

        # Return the total money saved after n days
        return ans
